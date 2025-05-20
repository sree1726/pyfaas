
print("Script has been loaded. Waiting for events...")  #This runs at load time

# from parliament import Context, event

# @event
# def main(context: Context):
#     print("Function 'main' started")  # This runs only on event trigger

#     otp_data = context.cloud_event.data
#     print(f"Event data: {otp_data}")

#     if isinstance(otp_data, dict) and "otp" in otp_data:
#         print(f"OTP received: {otp_data['otp']}")
#     else:
#         print("No OTP found in message!")

#     print("Function completed")
#     return {"status": "OTP processed"}
