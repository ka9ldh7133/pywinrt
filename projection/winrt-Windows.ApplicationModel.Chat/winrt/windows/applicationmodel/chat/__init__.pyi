# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

import enum
import datetime
import sys
import types
import typing

import winrt.system
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.media.mediaproperties
import winrt.windows.security.credentials
import winrt.windows.storage.streams

class ChatConversationThreadingKind(enum.IntEnum):
    PARTICIPANTS = 0
    CONTACT_ID = 1
    CONVERSATION_ID = 2
    CUSTOM = 3

class ChatItemKind(enum.IntEnum):
    MESSAGE = 0
    CONVERSATION = 1

class ChatMessageChangeType(enum.IntEnum):
    MESSAGE_CREATED = 0
    MESSAGE_MODIFIED = 1
    MESSAGE_DELETED = 2
    CHANGE_TRACKING_LOST = 3

class ChatMessageKind(enum.IntEnum):
    STANDARD = 0
    FILE_TRANSFER_REQUEST = 1
    TRANSPORT_CUSTOM = 2
    JOINED_CONVERSATION = 3
    LEFT_CONVERSATION = 4
    OTHER_PARTICIPANT_JOINED_CONVERSATION = 5
    OTHER_PARTICIPANT_LEFT_CONVERSATION = 6

class ChatMessageOperatorKind(enum.IntEnum):
    UNSPECIFIED = 0
    SMS = 1
    MMS = 2
    RCS = 3

class ChatMessageStatus(enum.IntEnum):
    DRAFT = 0
    SENDING = 1
    SENT = 2
    SEND_RETRY_NEEDED = 3
    SEND_FAILED = 4
    RECEIVED = 5
    RECEIVE_DOWNLOAD_NEEDED = 6
    RECEIVE_DOWNLOAD_FAILED = 7
    RECEIVE_DOWNLOADING = 8
    DELETED = 9
    DECLINED = 10
    CANCELLED = 11
    RECALLED = 12
    RECEIVE_RETRY_NEEDED = 13

class ChatMessageTransportKind(enum.IntEnum):
    TEXT = 0
    UNTRIAGED = 1
    BLOCKED = 2
    CUSTOM = 3

class ChatMessageValidationStatus(enum.IntEnum):
    VALID = 0
    NO_RECIPIENTS = 1
    INVALID_DATA = 2
    MESSAGE_TOO_LARGE = 3
    TOO_MANY_RECIPIENTS = 4
    TRANSPORT_INACTIVE = 5
    TRANSPORT_NOT_FOUND = 6
    TOO_MANY_ATTACHMENTS = 7
    INVALID_RECIPIENTS = 8
    INVALID_BODY = 9
    INVALID_OTHER = 10
    VALID_WITH_LARGE_MESSAGE = 11
    VOICE_ROAMING_RESTRICTION = 12
    DATA_ROAMING_RESTRICTION = 13

class ChatRestoreHistorySpan(enum.IntEnum):
    LAST_MONTH = 0
    LAST_YEAR = 1
    ANY_TIME = 2

class ChatStoreChangedEventKind(enum.IntEnum):
    NOTIFICATIONS_MISSED = 0
    STORE_MODIFIED = 1
    MESSAGE_CREATED = 2
    MESSAGE_MODIFIED = 3
    MESSAGE_DELETED = 4
    CONVERSATION_MODIFIED = 5
    CONVERSATION_DELETED = 6
    CONVERSATION_TRANSPORT_DELETED = 7

class ChatTransportErrorCodeCategory(enum.IntEnum):
    NONE = 0
    HTTP = 1
    NETWORK = 2
    MMS_SERVER = 3

class ChatTransportInterpretedErrorCode(enum.IntEnum):
    NONE = 0
    UNKNOWN = 1
    INVALID_RECIPIENT_ADDRESS = 2
    NETWORK_CONNECTIVITY = 3
    SERVICE_DENIED = 4
    TIMEOUT = 5

class RcsServiceKind(enum.IntEnum):
    CHAT = 0
    GROUP_CHAT = 1
    FILE_TRANSFER = 2
    CAPABILITY = 3

Self = typing.TypeVar('Self')

class ChatCapabilities(winrt.system.Object):
    is_chat_capable: winrt.system.Boolean
    is_file_transfer_capable: winrt.system.Boolean
    is_geo_location_push_capable: winrt.system.Boolean
    is_integrated_messaging_capable: winrt.system.Boolean
    is_online: winrt.system.Boolean
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatCapabilities: ...

class ChatCapabilitiesManager(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatCapabilitiesManager: ...
    @typing.overload
    @staticmethod
    def get_cached_capabilities_async(address: str, /) -> winrt.windows.foundation.IAsyncOperation[ChatCapabilities]: ...
    @typing.overload
    @staticmethod
    def get_cached_capabilities_async(address: str, transport_id: str, /) -> winrt.windows.foundation.IAsyncOperation[ChatCapabilities]: ...
    @typing.overload
    @staticmethod
    def get_capabilities_from_network_async(address: str, /) -> winrt.windows.foundation.IAsyncOperation[ChatCapabilities]: ...
    @typing.overload
    @staticmethod
    def get_capabilities_from_network_async(address: str, transport_id: str, /) -> winrt.windows.foundation.IAsyncOperation[ChatCapabilities]: ...

class ChatConversation(winrt.system.Object):
    subject: str
    is_conversation_muted: winrt.system.Boolean
    has_unread_messages: winrt.system.Boolean
    id: str
    most_recent_message_id: str
    participants: typing.Optional[winrt.windows.foundation.collections.IVector[str]]
    threading_info: typing.Optional[ChatConversationThreadingInfo]
    can_modify_participants: winrt.system.Boolean
    item_kind: ChatItemKind
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatConversation: ...
    def delete_async(self) -> winrt.windows.foundation.IAsyncAction: ...
    def get_message_reader(self) -> typing.Optional[ChatMessageReader]: ...
    @typing.overload
    def mark_messages_as_read_async(self) -> winrt.windows.foundation.IAsyncAction: ...
    @typing.overload
    def mark_messages_as_read_async(self, value: datetime.datetime, /) -> winrt.windows.foundation.IAsyncAction: ...
    def notify_local_participant_composing(self, transport_id: str, participant_address: str, is_composing: winrt.system.Boolean, /) -> None: ...
    def notify_remote_participant_composing(self, transport_id: str, participant_address: str, is_composing: winrt.system.Boolean, /) -> None: ...
    def save_async(self) -> winrt.windows.foundation.IAsyncAction: ...
    def add_remote_participant_composing_changed(self, handler: winrt.windows.foundation.TypedEventHandler[ChatConversation, RemoteParticipantComposingChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_remote_participant_composing_changed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class ChatConversationReader(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatConversationReader: ...
    @typing.overload
    def read_batch_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[ChatConversation]]: ...
    @typing.overload
    def read_batch_async(self, count: winrt.system.Int32, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[ChatConversation]]: ...

class ChatConversationThreadingInfo(winrt.system.Object):
    kind: ChatConversationThreadingKind
    custom: str
    conversation_id: str
    contact_id: str
    participants: typing.Optional[winrt.windows.foundation.collections.IVector[str]]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatConversationThreadingInfo: ...
    def __new__(cls: typing.Type[ChatConversationThreadingInfo]) -> ChatConversationThreadingInfo:...

class ChatMessage(winrt.system.Object):
    item_kind: ChatItemKind
    is_incoming: winrt.system.Boolean
    is_forwarding_disabled: winrt.system.Boolean
    transport_id: str
    status: ChatMessageStatus
    from_: str
    body: str
    subject: str
    is_read: winrt.system.Boolean
    network_timestamp: datetime.datetime
    local_timestamp: datetime.datetime
    recipient_send_statuses: typing.Optional[winrt.windows.foundation.collections.IMapView[str, ChatMessageStatus]]
    recipients: typing.Optional[winrt.windows.foundation.collections.IVector[str]]
    transport_friendly_name: str
    attachments: typing.Optional[winrt.windows.foundation.collections.IVector[ChatMessageAttachment]]
    id: str
    is_seen: winrt.system.Boolean
    message_kind: ChatMessageKind
    is_received_during_quiet_hours: winrt.system.Boolean
    is_auto_reply: winrt.system.Boolean
    estimated_download_size: winrt.system.UInt64
    threading_info: typing.Optional[ChatConversationThreadingInfo]
    should_suppress_notification: winrt.system.Boolean
    remote_id: str
    message_operator_kind: ChatMessageOperatorKind
    is_reply_disabled: winrt.system.Boolean
    is_sim_message: winrt.system.Boolean
    recipients_delivery_infos: typing.Optional[winrt.windows.foundation.collections.IVector[ChatRecipientDeliveryInfo]]
    sync_id: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessage: ...
    def __new__(cls: typing.Type[ChatMessage]) -> ChatMessage:...

class ChatMessageAttachment(winrt.system.Object):
    text: str
    mime_type: str
    group_id: winrt.system.UInt32
    data_stream_reference: typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]
    transfer_progress: winrt.system.Double
    thumbnail: typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]
    original_file_name: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessageAttachment: ...
    def __new__(cls: typing.Type[ChatMessageAttachment], mime_type: str, data_stream_reference: typing.Optional[winrt.windows.storage.streams.IRandomAccessStreamReference]) -> ChatMessageAttachment:...

class ChatMessageBlocking(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessageBlocking: ...
    @staticmethod
    def mark_message_as_blocked_async(local_chat_message_id: str, blocked: winrt.system.Boolean, /) -> winrt.windows.foundation.IAsyncAction: ...

class ChatMessageChange(winrt.system.Object):
    change_type: ChatMessageChangeType
    message: typing.Optional[ChatMessage]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessageChange: ...

class ChatMessageChangeReader(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessageChangeReader: ...
    def accept_changes(self) -> None: ...
    def accept_changes_through(self, last_change_to_acknowledge: typing.Optional[ChatMessageChange], /) -> None: ...
    def read_batch_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[ChatMessageChange]]: ...

class ChatMessageChangeTracker(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessageChangeTracker: ...
    def enable(self) -> None: ...
    def get_change_reader(self) -> typing.Optional[ChatMessageChangeReader]: ...
    def reset(self) -> None: ...

class ChatMessageChangedDeferral(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessageChangedDeferral: ...
    def complete(self) -> None: ...

class ChatMessageChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessageChangedEventArgs: ...
    def get_deferral(self) -> typing.Optional[ChatMessageChangedDeferral]: ...

class ChatMessageManager(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessageManager: ...
    @staticmethod
    def get_transport_async(transport_id: str, /) -> winrt.windows.foundation.IAsyncOperation[ChatMessageTransport]: ...
    @staticmethod
    def get_transports_async() -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[ChatMessageTransport]]: ...
    @staticmethod
    def register_transport_async() -> winrt.windows.foundation.IAsyncOperation[str]: ...
    @staticmethod
    def request_store_async() -> winrt.windows.foundation.IAsyncOperation[ChatMessageStore]: ...
    @staticmethod
    def request_sync_manager_async() -> winrt.windows.foundation.IAsyncOperation[ChatSyncManager]: ...
    @staticmethod
    def show_compose_sms_message_async(message: typing.Optional[ChatMessage], /) -> winrt.windows.foundation.IAsyncAction: ...
    @staticmethod
    def show_sms_settings() -> None: ...

class ChatMessageNotificationTriggerDetails(winrt.system.Object):
    chat_message: typing.Optional[ChatMessage]
    should_display_toast: winrt.system.Boolean
    should_update_action_center: winrt.system.Boolean
    should_update_badge: winrt.system.Boolean
    should_update_detail_text: winrt.system.Boolean
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessageNotificationTriggerDetails: ...

class ChatMessageReader(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessageReader: ...
    @typing.overload
    def read_batch_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[ChatMessage]]: ...
    @typing.overload
    def read_batch_async(self, count: winrt.system.Int32, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[ChatMessage]]: ...

class ChatMessageStore(winrt.system.Object):
    change_tracker: typing.Optional[ChatMessageChangeTracker]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessageStore: ...
    def delete_message_async(self, local_message_id: str, /) -> winrt.windows.foundation.IAsyncAction: ...
    def download_message_async(self, local_chat_message_id: str, /) -> winrt.windows.foundation.IAsyncAction: ...
    def forward_message_async(self, local_chat_message_id: str, addresses: typing.Iterable[str], /) -> winrt.windows.foundation.IAsyncOperation[ChatMessage]: ...
    @typing.overload
    def get_conversation_async(self, conversation_id: str, /) -> winrt.windows.foundation.IAsyncOperation[ChatConversation]: ...
    @typing.overload
    def get_conversation_async(self, conversation_id: str, transport_ids: typing.Iterable[str], /) -> winrt.windows.foundation.IAsyncOperation[ChatConversation]: ...
    def get_conversation_from_threading_info_async(self, threading_info: typing.Optional[ChatConversationThreadingInfo], /) -> winrt.windows.foundation.IAsyncOperation[ChatConversation]: ...
    @typing.overload
    def get_conversation_reader(self) -> typing.Optional[ChatConversationReader]: ...
    @typing.overload
    def get_conversation_reader(self, transport_ids: typing.Iterable[str], /) -> typing.Optional[ChatConversationReader]: ...
    def get_message_async(self, local_chat_message_id: str, /) -> winrt.windows.foundation.IAsyncOperation[ChatMessage]: ...
    def get_message_by_remote_id_async(self, transport_id: str, remote_id: str, /) -> winrt.windows.foundation.IAsyncOperation[ChatMessage]: ...
    def get_message_by_sync_id_async(self, sync_id: str, /) -> winrt.windows.foundation.IAsyncOperation[ChatMessage]: ...
    @typing.overload
    def get_message_reader(self) -> typing.Optional[ChatMessageReader]: ...
    @typing.overload
    def get_message_reader(self, recent_time_limit: datetime.timedelta, /) -> typing.Optional[ChatMessageReader]: ...
    def get_search_reader(self, value: typing.Optional[ChatQueryOptions], /) -> typing.Optional[ChatSearchReader]: ...
    @typing.overload
    def get_unseen_count_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.system.Int32]: ...
    @typing.overload
    def get_unseen_count_async(self, transport_ids: typing.Iterable[str], /) -> winrt.windows.foundation.IAsyncOperation[winrt.system.Int32]: ...
    @typing.overload
    def mark_as_seen_async(self) -> winrt.windows.foundation.IAsyncAction: ...
    @typing.overload
    def mark_as_seen_async(self, transport_ids: typing.Iterable[str], /) -> winrt.windows.foundation.IAsyncAction: ...
    def mark_message_read_async(self, local_chat_message_id: str, /) -> winrt.windows.foundation.IAsyncAction: ...
    def retry_send_message_async(self, local_chat_message_id: str, /) -> winrt.windows.foundation.IAsyncAction: ...
    def save_message_async(self, chat_message: typing.Optional[ChatMessage], /) -> winrt.windows.foundation.IAsyncAction: ...
    def send_message_async(self, chat_message: typing.Optional[ChatMessage], /) -> winrt.windows.foundation.IAsyncAction: ...
    def try_cancel_download_message_async(self, local_chat_message_id: str, /) -> winrt.windows.foundation.IAsyncOperation[winrt.system.Boolean]: ...
    def try_cancel_send_message_async(self, local_chat_message_id: str, /) -> winrt.windows.foundation.IAsyncOperation[winrt.system.Boolean]: ...
    def validate_message(self, chat_message: typing.Optional[ChatMessage], /) -> typing.Optional[ChatMessageValidationResult]: ...
    def add_message_changed(self, value: winrt.windows.foundation.TypedEventHandler[ChatMessageStore, ChatMessageChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_message_changed(self, value: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...
    def add_store_changed(self, handler: winrt.windows.foundation.TypedEventHandler[ChatMessageStore, ChatMessageStoreChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_store_changed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class ChatMessageStoreChangedEventArgs(winrt.system.Object):
    id: str
    kind: ChatStoreChangedEventKind
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessageStoreChangedEventArgs: ...

class ChatMessageTransport(winrt.system.Object):
    is_active: winrt.system.Boolean
    is_app_set_as_notification_provider: winrt.system.Boolean
    transport_friendly_name: str
    transport_id: str
    configuration: typing.Optional[ChatMessageTransportConfiguration]
    transport_kind: ChatMessageTransportKind
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessageTransport: ...
    def request_set_as_notification_provider_async(self) -> winrt.windows.foundation.IAsyncAction: ...

class ChatMessageTransportConfiguration(winrt.system.Object):
    extended_properties: typing.Optional[winrt.windows.foundation.collections.IMapView[str, winrt.system.Object]]
    max_attachment_count: winrt.system.Int32
    max_message_size_in_kilobytes: winrt.system.Int32
    max_recipient_count: winrt.system.Int32
    supported_video_format: typing.Optional[winrt.windows.media.mediaproperties.MediaEncodingProfile]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessageTransportConfiguration: ...

class ChatMessageValidationResult(winrt.system.Object):
    max_part_count: typing.Optional[typing.Optional[winrt.system.UInt32]]
    part_count: typing.Optional[typing.Optional[winrt.system.UInt32]]
    remaining_character_count_in_part: typing.Optional[typing.Optional[winrt.system.UInt32]]
    status: ChatMessageValidationStatus
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatMessageValidationResult: ...

class ChatQueryOptions(winrt.system.Object):
    search_string: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatQueryOptions: ...
    def __new__(cls: typing.Type[ChatQueryOptions]) -> ChatQueryOptions:...

class ChatRecipientDeliveryInfo(winrt.system.Object):
    transport_address: str
    read_time: typing.Optional[typing.Optional[datetime.datetime]]
    delivery_time: typing.Optional[typing.Optional[datetime.datetime]]
    is_error_permanent: winrt.system.Boolean
    status: ChatMessageStatus
    transport_error_code: winrt.system.Int32
    transport_error_code_category: ChatTransportErrorCodeCategory
    transport_interpreted_error_code: ChatTransportInterpretedErrorCode
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatRecipientDeliveryInfo: ...
    def __new__(cls: typing.Type[ChatRecipientDeliveryInfo]) -> ChatRecipientDeliveryInfo:...

class ChatSearchReader(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatSearchReader: ...
    @typing.overload
    def read_batch_async(self) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[IChatItem]]: ...
    @typing.overload
    def read_batch_async(self, count: winrt.system.Int32, /) -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[IChatItem]]: ...

class ChatSyncConfiguration(winrt.system.Object):
    restore_history_span: ChatRestoreHistorySpan
    is_sync_enabled: winrt.system.Boolean
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatSyncConfiguration: ...

class ChatSyncManager(winrt.system.Object):
    configuration: typing.Optional[ChatSyncConfiguration]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> ChatSyncManager: ...
    def associate_account_async(self, web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], /) -> winrt.windows.foundation.IAsyncAction: ...
    def is_account_associated(self, web_account: typing.Optional[winrt.windows.security.credentials.WebAccount], /) -> winrt.system.Boolean: ...
    def set_configuration_async(self, configuration: typing.Optional[ChatSyncConfiguration], /) -> winrt.windows.foundation.IAsyncAction: ...
    def start_sync(self) -> None: ...
    def unassociate_account_async(self) -> winrt.windows.foundation.IAsyncAction: ...

class RcsEndUserMessage(winrt.system.Object):
    actions: typing.Optional[winrt.windows.foundation.collections.IVectorView[RcsEndUserMessageAction]]
    is_pin_required: winrt.system.Boolean
    text: str
    title: str
    transport_id: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> RcsEndUserMessage: ...
    def send_response_async(self, action: typing.Optional[RcsEndUserMessageAction], /) -> winrt.windows.foundation.IAsyncAction: ...
    def send_response_with_pin_async(self, action: typing.Optional[RcsEndUserMessageAction], pin: str, /) -> winrt.windows.foundation.IAsyncAction: ...

class RcsEndUserMessageAction(winrt.system.Object):
    label: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> RcsEndUserMessageAction: ...

class RcsEndUserMessageAvailableEventArgs(winrt.system.Object):
    is_message_available: winrt.system.Boolean
    message: typing.Optional[RcsEndUserMessage]
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> RcsEndUserMessageAvailableEventArgs: ...

class RcsEndUserMessageAvailableTriggerDetails(winrt.system.Object):
    text: str
    title: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> RcsEndUserMessageAvailableTriggerDetails: ...

class RcsEndUserMessageManager(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> RcsEndUserMessageManager: ...
    def add_message_available_changed(self, handler: winrt.windows.foundation.TypedEventHandler[RcsEndUserMessageManager, RcsEndUserMessageAvailableEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_message_available_changed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class RcsManager(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> RcsManager: ...
    @staticmethod
    def get_end_user_message_manager() -> typing.Optional[RcsEndUserMessageManager]: ...
    @staticmethod
    def get_transport_async(transport_id: str, /) -> winrt.windows.foundation.IAsyncOperation[RcsTransport]: ...
    @staticmethod
    def get_transports_async() -> winrt.windows.foundation.IAsyncOperation[winrt.windows.foundation.collections.IVectorView[RcsTransport]]: ...
    @staticmethod
    def leave_conversation_async(conversation: typing.Optional[ChatConversation], /) -> winrt.windows.foundation.IAsyncAction: ...
    @staticmethod
    def add_transport_list_changed(handler: winrt.windows.foundation.EventHandler[winrt.system.Object], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    @staticmethod
    def remove_transport_list_changed(token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class RcsServiceKindSupportedChangedEventArgs(winrt.system.Object):
    service_kind: RcsServiceKind
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> RcsServiceKindSupportedChangedEventArgs: ...

class RcsTransport(winrt.system.Object):
    configuration: typing.Optional[RcsTransportConfiguration]
    extended_properties: typing.Optional[winrt.windows.foundation.collections.IMapView[str, winrt.system.Object]]
    is_active: winrt.system.Boolean
    transport_friendly_name: str
    transport_id: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> RcsTransport: ...
    def is_service_kind_supported(self, service_kind: RcsServiceKind, /) -> winrt.system.Boolean: ...
    def is_store_and_forward_enabled(self, service_kind: RcsServiceKind, /) -> winrt.system.Boolean: ...
    def add_service_kind_supported_changed(self, handler: winrt.windows.foundation.TypedEventHandler[RcsTransport, RcsServiceKindSupportedChangedEventArgs], /) -> winrt.windows.foundation.EventRegistrationToken: ...
    def remove_service_kind_supported_changed(self, token: winrt.windows.foundation.EventRegistrationToken, /) -> None: ...

class RcsTransportConfiguration(winrt.system.Object):
    max_attachment_count: winrt.system.Int32
    max_file_size_in_kilobytes: winrt.system.Int32
    max_group_message_size_in_kilobytes: winrt.system.Int32
    max_message_size_in_kilobytes: winrt.system.Int32
    max_recipient_count: winrt.system.Int32
    warning_file_size_in_kilobytes: winrt.system.Int32
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> RcsTransportConfiguration: ...

class RemoteParticipantComposingChangedEventArgs(winrt.system.Object):
    is_composing: winrt.system.Boolean
    participant_address: str
    transport_id: str
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> RemoteParticipantComposingChangedEventArgs: ...

class IChatItem(winrt.system.Object):
    item_kind: ChatItemKind
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IChatItem: ...
