import logging

from sendmail import sendmail
from zenutils import importutils

from .settings import DJANGO_SITE_WARNING_NOTIFY_MAIL_CONFIG
from .settings import DJANGO_SITE_WARNING_NOTIFY_MAIL_FROM
from .settings import DJANGO_SITE_WARNING_NOTIFY_MAIL_TO
from .settings import DJANGO_SITE_WARNING_NOTIFY_MAIL_SERVER
from .settings import DJANGO_SITE_WARNING_NOTIFY_MAIL_PORT
from .settings import DJANGO_SITE_WARNING_NOTIFY_MAIL_SSL
from .settings import DJANGO_SITE_WARNING_NOTIFY_MAIL_USER
from .settings import DJANGO_SITE_WARNING_NOTIFY_MAIL_PASSWORD

_logger = logging.getLogger(__name__)


def sendmail_notify(warning, payload, force):
    _logger.debug(
        "django-site-warnings doing sendmail_notify...",
    )

    config = DJANGO_SITE_WARNING_NOTIFY_MAIL_CONFIG
    if config and isinstance(config, str):
        config_callback = importutils.import_from_string(config)
        if config_callback and callable(config_callback):
            config = config_callback(warning, payload, force)
    if not config:
        config = {
            "from_address": DJANGO_SITE_WARNING_NOTIFY_MAIL_FROM,
            "to_addresses": DJANGO_SITE_WARNING_NOTIFY_MAIL_TO,
            "server": DJANGO_SITE_WARNING_NOTIFY_MAIL_SERVER,
            "port": DJANGO_SITE_WARNING_NOTIFY_MAIL_PORT,
            "ssl": DJANGO_SITE_WARNING_NOTIFY_MAIL_SSL,
            "user": DJANGO_SITE_WARNING_NOTIFY_MAIL_USER,
            "password": DJANGO_SITE_WARNING_NOTIFY_MAIL_PASSWORD,
        }

    _logger.debug(
        "django-site-warnings doing sendmail_notify with config: %s",
        config,
    )

    subject = warning.get_notify_email_subject()
    content = warning.get_notify_email_content()

    sendmail(
        config["from_address"],
        config["to_addresses"],
        content,
        subject,
        attachs=None,
        is_html_content=True,
        encoding="utf-8",
        charset="utf-8",
        host=config["server"],
        port=config.get("port", 465),
        ssl=config.get("ssl", True),
        user=config["user"],
        password=config["password"],
    )
