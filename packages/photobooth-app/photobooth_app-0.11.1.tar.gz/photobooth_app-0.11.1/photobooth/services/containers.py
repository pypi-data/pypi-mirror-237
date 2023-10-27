"""Containers module."""


import logging

from dependency_injector import containers, providers
from pymitter import EventEmitter

from ..appconfig import AppConfig
from .aquisitionservice import AquisitionService
from .gpioservice import GpioService
from .informationservice import InformationService
from .keyboardservice import KeyboardService
from .mediacollectionservice import MediacollectionService
from .mediaprocessingservice import MediaprocessingService
from .printingservice import PrintingService
from .processingservice import ProcessingService
from .shareservice import ShareService
from .sseservice import SseService
from .systemservice import SystemService
from .wledservice import WledService

logger = logging.getLogger(__name__)


def init_aquisition_resource(evtbus, config, primary_backend, secondary_backend):
    resource = AquisitionService(
        evtbus=evtbus,
        config=config,
        primary_backend=primary_backend,
        secondary_backend=secondary_backend,
    )
    try:
        resource.start()
    except Exception as exc:
        logger.critical(f"failed to start acquisition {exc}")
        raise RuntimeError(f"cannot start backend, app fails, check configuration {exc}") from exc
    else:
        yield resource
    finally:
        resource.stop()


def init_information_resource(evtbus, config):
    resource = InformationService(evtbus=evtbus, config=config)
    resource.start()
    yield resource
    resource.stop()


def init_wled_resource(evtbus, config):
    resource = WledService(evtbus=evtbus, config=config)
    try:
        resource.start()
    except RuntimeError as wledservice_exc:
        # catch exception to make app continue without wled service in case there is a connection problem
        logging.warning(f"WLED module init failed {wledservice_exc}")
        raise wledservice_exc
    else:
        yield resource
        resource.stop()
    finally:
        pass


def init_gpio_resource(evtbus, config, processing_service, printing_service, mediacollection_service):
    resource = GpioService(
        evtbus=evtbus,
        config=config,
        processing_service=processing_service,
        printing_service=printing_service,
        mediacollection_service=mediacollection_service,
    )
    resource.start()
    yield resource
    resource.stop()


def init_share_resource(evtbus, config, mediacollection_service):
    resource = ShareService(evtbus=evtbus, config=config, mediacollection_service=mediacollection_service)
    resource.start()
    yield resource
    resource.stop()


class ServicesContainer(containers.DeclarativeContainer):
    evtbus = providers.Dependency(instance_of=EventEmitter)
    config = providers.Dependency(instance_of=AppConfig)
    backends = providers.DependenciesContainer()

    # Services: Core

    aquisition_service = providers.Resource(
        init_aquisition_resource,
        evtbus=evtbus,
        config=config,
        primary_backend=backends.primary_backend,
        secondary_backend=backends.secondary_backend,
    )

    sse_service = providers.Singleton(SseService, evtbus=evtbus, config=config)

    information_service = providers.Resource(init_information_resource, evtbus=evtbus, config=config)

    mediaprocessing_service = providers.Singleton(
        MediaprocessingService,
        evtbus=evtbus,
        config=config,
    )
    mediacollection_service = providers.Singleton(
        MediacollectionService,
        evtbus=evtbus,
        config=config,
        mediaprocessing_service=mediaprocessing_service,
    )

    processing_service = providers.Singleton(
        ProcessingService,
        evtbus=evtbus,
        config=config,
        aquisition_service=aquisition_service,
        mediacollection_service=mediacollection_service,
        mediaprocessing_service=mediaprocessing_service,
    )

    system_service = providers.Factory(SystemService, evtbus=evtbus, config=config)

    wled_service = providers.Resource(
        init_wled_resource,
        evtbus=evtbus,
        config=config,
    )

    printing_service = providers.Resource(
        PrintingService,
        evtbus=evtbus,
        config=config,
        mediacollection_service=mediacollection_service,
    )

    keyboard_service = providers.Resource(
        KeyboardService,
        evtbus=evtbus,
        config=config,
        processing_service=processing_service,
        printing_service=printing_service,
        mediacollection_service=mediacollection_service,
    )

    gpio_service = providers.Resource(
        init_gpio_resource,
        evtbus=evtbus,
        config=config,
        processing_service=processing_service,
        printing_service=printing_service,
        mediacollection_service=mediacollection_service,
    )

    share_service = providers.Resource(
        init_share_resource,
        evtbus=evtbus,
        config=config,
        mediacollection_service=mediacollection_service,
    )
