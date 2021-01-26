# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sms_sample.py
DESCRIPTION:
    These samples demonstrate sending an sms.
    
    ///authenticating a client via a connection string
USAGE:
    python sms_sample.py
"""

import sys
from azure.communication.sms import (
    SendSmsOptions, PhoneNumberIdentifier, SmsClient
)

sys.path.append("..")

class SmsSamples(object):

    def send_sms(self):
        connection_string = "COMMUNICATION_SERVICES_CONNECTION_STRING"

        sms_client = SmsClient.from_connection_string(connection_string)

        # calling send() with sms values
        sms_responses = sms_client.send(
            from_phone_number="<leased-phone-number>",
            to_phone_numbers=["<to-phone-number-1>", "<to-phone-number-2>", "<to-phone-number-3>"],
            message="Hello World via SMS",
            send_sms_options=SendSmsOptions(enable_delivery_report=True, tag="custom-tag")) # optional property

        for sms_response in sms_responses:
            print(sms_response)

if __name__ == '__main__':
    sample = SmsSamples()
    sample.send_sms()
