# from parliament import Context, event


# @event
# def main(context: Context):
#     """
#     Function template
#     The context parameter contains the Flask request object and any
#     CloudEvent received with the request.
#     """

#     # Add your business logic here

#     # The return value here will be applied as the data attribute
#     # of a CloudEvent returned to the function invoker
#     return context.cloud_event.data


from parliament import Context, event

@event
def main(context: Context):
    print("Function 'main' started")  # Start log

    otp_data = context.cloud_event.data
    print(f"📦 Received event data: {otp_data}")  # Debug input

    if isinstance(otp_data, dict) and "otp" in otp_data:
        print(f"🔐 OTP received: {otp_data['otp']}")
    else:
        print("⚠️ No OTP found in message!")

    print("Function 'main' completed")  # End log
    return {"status": "OTP processed"}



# from cloudevents.http import CloudEvent
 
# def main(event: CloudEvent) -> dict:
#     otp_data = event.data  # Corrected access
 
#     if isinstance(otp_data, dict) and "otp" in otp_data:
#         print(f"🔐 OTP received: {otp_data['otp']}")
#     else:
#         print("⚠️ No OTP found in message!")
 
#     return {"status": "OTP processed"}
