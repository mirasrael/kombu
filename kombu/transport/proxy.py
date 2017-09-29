from __future__ import absolute_import

from .base import StdChannel


class ProxyChannel(StdChannel):
    def __init__(self, channel_getter):
        self._channel_getter = channel_getter

    @property
    def connection(self):
        return self._channel_getter().connection

    @property
    def events(self):
        return self._channel_getter().events

    @property
    def channel_id(self):
        return self._channel_getter().channel_id

    @property
    def open(self):
        return self._channel_getter().open

    def exchange_declare(self, *args, **kwargs):
        return self._channel_getter().exchange_declare(*args, **kwargs)

    def prepare_message(self, *args, **kwargs):
        return self._channel_getter().prepare_message(*args, **kwargs)

    def basic_publish(self, *args, **kwargs):
        return self._channel_getter().basic_publish(*args, **kwargs)

    def exchange_delete(self, *args, **kwargs):
        return self._channel_getter().exchange_delete(*args, **kwargs)

    def queue_declare(self, *args, **kwargs):
        return self._channel_getter().queue_declare(*args, **kwargs)

    def queue_bind(self, *args, **kwargs):
        return self._channel_getter().queue_bind(*args, **kwargs)

    def queue_unbind(self, *args, **kwargs):
        return self._channel_getter().queue_unbind(*args, **kwargs)

    def queue_delete(self, *args, **kwargs):
        return self._channel_getter().queue_delete(*args, **kwargs)

    def basic_get(self, *args, **kwargs):
        return self._channel_getter().basic_get(*args, **kwargs)

    def queue_purge(self, *args, **kwargs):
        return self._channel_getter().queue_purge(*args, **kwargs)

    def basic_consume(self, *args, **kwargs):
        return self._channel_getter().basic_consume(*args, **kwargs)

    def basic_cancel(self, *args, **kwargs):
        return self._channel_getter().basic_cancel(*args, **kwargs)

    def basic_ack(self, *args, **kwargs):
        return self._channel_getter().basic_ack(*args, **kwargs)

    def basic_recover(self, *args, **kwargs):
        return self._channel_getter().basic_recover(*args, **kwargs)

    def exchange_bind(self, *args, **kwargs):
        return self._channel_getter().exchange_bind(*args, **kwargs)

    def exchange_unbind(self, *args, **kwargs):
        return self._channel_getter().exchange_unbind(*args, **kwargs)

    def close(self, *args, **kwargs):
        self._channel_getter().close(*args, **kwargs)

    def message_to_python(self, *args, **kwargs):
        return self._channel_getter().message_to_python(*args, **kwargs)

    def flow(self, *args, **kwargs):
        return self._channel_getter().flow(*args, **kwargs)

    def basic_reject(self, *args, **kwargs):
        return self._channel_getter().basic_reject(*args, **kwargs)

    def basic_qos(self, *args, **kwargs):
        return self._channel_getter().basic_qos(*args, **kwargs)
