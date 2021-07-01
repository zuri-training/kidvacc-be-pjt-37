from paystackapi.paystack import Transaction
from paystackapi.charge import Charge
from dotenv import load_dotenv
import os
load_dotenv()
paystack_secret_key = os.environ.get('PAYSTACK_SECRET_KEY')

paystack_charge = Charge(secret_key=paystack_secret_key)

   
response = paystack_charge.start_charge( email="katchyemma@gmail.com",amount="450", bank={"account_number":"0000000000","code":"057"},birthday="1995-04-03")
print(response)
    
# reference = response['data']['reference']
    
# response3 = paystack_charge.submit_otp(otp="123456",reference=reference)

# response2 = paystack_charge.submit_pin(pin ='0888',reference=reference)

# response3 = paystack_charge.submit_otp(otp="123456",reference=reference)

# response4 = paystack_charge.submit_birthday(birthday="1995-12-23", reference=reference)

# response5 = paystack_charge.check_pending(reference=reference)

# print({ "status":response5['data']['status'],"reference":response5['data']['reference'],"gateway_response":response5['data']['gateway_response'],'paid_at':response5['data']['paid_at'], "email":response5['data']['customer']['email'],'amount':response5['data']['amount']})

