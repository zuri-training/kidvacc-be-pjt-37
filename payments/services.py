from paystackapi.paystack import Transaction
from paystackapi.charge import Charge
from dotenv import load_dotenv
import os
load_dotenv()
paystack_secret_key = os.environ.get('PAYSTACK_SECRET_KEY')

paystack_charge = Charge(secret_key=paystack_secret_key)

def charge_user(amt,email,bank,birthday, **kwargs):
   
    response = paystack_charge.start_charge( email=email,amount=amt, bank=bank,
         birthday=birthday,)
    print(response)
    
    reference = response['data']['reference']
    
    response3 = paystack_charge.submit_otp(otp="123456",reference=reference)
    print(response3)
    response2 = paystack_charge.submit_pin(pin ='0888',reference=reference)
    print(response2)
    response3 = paystack_charge.submit_otp(otp="123456",reference=reference)
    print(response3)
    response4 = paystack_charge.submit_birthday(birthday="1995-12-23", reference=reference)
    print(response4)
    response5 = paystack_charge.check_pending(reference=reference)
    print(response5)
    amount = response5['data']['amount']
    charge_status = response5['data']['gateway_response']

    return { "status":response5['data']['status'],"reference":response5['data']['reference'],"gateway_response":response5['data']['gateway_response'],'paid_at':response5['data']['paid_at'], "email":response5['data']['customer']['email']}

