from termii_sdk import TermiiSDK
from termii_sdk.core import Request

# Default sdk termii_enpoint
# TERMII_ENDPOINT = "https://api.ng.termii.com/api"

Request.termii_endpoint = 'your termii endpoint'

# Initialize the SDK with your API key
api_key = "your_api_key_here"
termii = TermiiSDK(api_key)

# Send an SMS message
message = "Hello from Termii SDK!"
phone_number = "+1234567890"
response = termii.send_message(to=phone_number, sms=message)
print("Message ID:", response.get("message_id"))
from termii_sdk import *
from termii_sdk import *

api_key = "TLc1jHchbxRi2K4hha38DmtHJWbIzR4GwGv9ieOXAXPRSG8dDFlKDQh2nKoa55"
termii = TermiiSDK(api_key)


response: Union[Error, BalanceResponse] = termii.balance()

response: Union[Error, SearchResponse] = termii.search()

response: Union[Error, StatusResponse] = termii.status()

response: Union[Error, HistoryResponse] = termii.history()

response: Union[Error, Response] = termii.send_campaign(
        country_code: str,
        sender_id: str,
        message: str,
        channel: Channel,
        message_type: MessageType,
        phonebook_id: str,
        delimiter: str,
        remove_duplicate: str,
        campaign_type: str,
        schedule_time: str = "",
        schedule_sms_status: str = "",
    )

response: Union[Error, FetchCampaignsResponse] = termii.fetch_campaigns()

response: Union[Error, FetchCampaignsHistoryResponse] = termii.fetch_campaign_history(campaign_id: str)


response: Union[Error, FetchPhonebooksResponse]: = termii.fetch_contacts(phonebook_id: str)

response: Union[Error, AddContactResponse]: = termii.add_contact(
        phonebook_id: str,
        phone_number: str,
        email_address: str,
        first_name: str,
        last_name: str,
        company: str,
        country_code: str,
    )

response: Union[Error, Response]: = termii.add_contacts(
        phonebook_id: str,
        contact_file: str,
        country_code: str,
    )

response: Union[Error, Response]: = termii.delete_contact_phonebook(contact_id: str)



response: Union[Error, BasicResponse]: = termii.send_message(
        to: str,
        from_: str,
        channel: Channel = Channel.GENERIC,
        sms: str = "",
        type: MediaType = MediaType.PLAIN,
        media_url: str = "",
        media_caption: str = "",
    )

response: Union[Error, BasicResponse]: = termii.send_bulk_message(
        to: list[str],
        from_: str,
        channel: Channel = Channel.GENERIC,
        sms: str = "",
    )




response: Union[Error, BasicResponse]: = termii.send_message_number(
        to: str,
        sms: str = "",
    )

response: Union[Error, FetchPhonebooksResponse]: = termii.fetch_phonebooks()

response: Union[Error, Response]: = termii.create_phonebook(
        phonebook_name: str,
        description: str,
    )

response: Union[Error, Response]: = termii.update_phonebook(
        phonebook_id: str,
        phonebook_name: str,
        description: str,
    )

response: Union[Error, FetchSenderIDResponse]: = termii.fetch_id()

response: Union[Error, Response]: = termii.request_id(
        sender_id: str,
        usecase: str,
        company: str,
    )

response: Union[Error, BasicResponse]: = termii.device_template(
        phone_number: str,
        device_id: str,
        template_id: str,
        data: dict = None,
    )

response: Union[Error, SendTokenResponse]: = termii.send_token(
        message_type: MessageType,
        to: str,
        from_: str,
        channel: Channel,
        pin_attempts: int,
        pin_time_to_live: int,
        pin_length: int,
        pin_placeholder: str,
        message_text: str,
        pin_type: MessageType,
    )

response: Union[Error, VoiceTokenResponse]: = termii.voice_token(
        phone_number: str,
        pin_attempts: str,
        pin_time_to_live: str,
        pin_length: str,
    )

response: Union[Error, VoiceCallResponse]: = termii.voice_call(
        phone_number: str,
        code: int,
    )

response: Union[Error, InAppTokenResponse]: = termii.in_app_token(
        phone_number: str,
        pin_type: MessageType,
        pin_attempts: int,
        pin_time_to_live: int,
        pin_length: int,
    )

response: Union[Error, VerifyTokenResponse]: = termii.verify_token(
        pin_id: str,
        pin: str,
    )

response: Union[Error, EmailTokenResponse]: = termii.email_token(
        email_address: str,
        code: str,
        email_configuration_id: str,
    )


