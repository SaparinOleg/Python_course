class Telephone:
    phone_number = ''
    _call_counter = 0

    def set_number(self, number):
        self.phone_number = number

    def incoming_call(self):
        self._call_counter += 1

    def get_calls_amount(self):
        return self._call_counter


def calls_to_file(phones: list):
    with open('call_list.csv', 'w') as call_list:
        print(f'Phone number, Calls', file=call_list)
        total = 0
        for phone in phones:
            print(f'{phone.phone_number}, {phone.get_calls_amount()}', file=call_list)
            total += phone.get_calls_amount()
        print(f'Total, {total}', file=call_list)


def amount_of_calls(phones: list):
    return sum(phone.get_calls_amount() for phone in phones)


phone1 = Telephone()
phone1.set_number(80631451414)
phone1.incoming_call()
phone1.incoming_call()
phone1.incoming_call()
phone1.incoming_call()

phone2 = Telephone()
phone2.set_number(80666666666)
for calls in range(25):
    phone2.incoming_call()

phone3 = Telephone()
phone3.set_number(80501234567)
for calls in range(16):
    phone3.incoming_call()

print(f'Total calls: {amount_of_calls([phone1, phone2, phone3])}')
calls_to_file([phone1, phone2, phone3])
