bot_list = []
output_list = []


def get_or_create_bot(id):
    for bot in bot_list:
        if bot.ID == id:
            return bot

    ret = Bot(id)
    bot_list.append(ret)
    return ret


def get_or_create_output(id):
    for output in output_list:
        if output.ID == id:
            return output

    ret = Output(id)
    output_list.append(ret)
    return ret


class Bot(object):
    def __init__(self, id):
        self.ID = id
        self.instructions = []
        self.chips = []

    def do_instruction(self):
        low_recv_type, low_recv_id, high_recv_type, high_recv_id = self.instructions[0]
        self.instructions.pop(0)
        if low_recv_type == 'bot':
            low_recv = get_or_create_bot(low_recv_id)
        else:
            low_recv = get_or_create_output(low_recv_id)

        if high_recv_type == 'bot':
            high_recv = get_or_create_bot(high_recv_id)
        else:
            high_recv = get_or_create_output(high_recv_id)

        low, high = min(self.chips), max(self.chips)

        low_recv.recv(low)
        high_recv.recv(high)
        self.chips = []

    def recv(self, chip_val):
        self.chips.append(chip_val)

        if self.is_ready():
            self.do_instruction()

    def is_ready(self):
        if len(self.chips) < 2 or len(self.instructions) < 1:
            return False
        return True


class Output(object):
    def __init__(self, id):
        self.ID = id
        self.chips = []

    def recv(self, chip_val):
        self.chips.append(chip_val)


with open('10.txt', 'r') as file:
    for line in file.readlines():
        if line.startswith('bot'):
            words = line.strip().split(' ')
            bot_id = int(words[1])
            low_recv_type, low_recv_id = words[5], int(words[6])
            high_recv_type, high_recv_id = words[10], int(words[11])

            bot = get_or_create_bot(bot_id)

            bot.instructions.append((low_recv_type, low_recv_id, high_recv_type, high_recv_id))

            if bot.is_ready():
                bot.do_instruction()

        elif line.startswith('value'):
            words = line.strip().split(' ')
            bot_id = int(words[5])
            chip = int(words[1])

            bot = get_or_create_bot(bot_id)
            bot.recv(chip)


result = sum(get_or_create_output(0).chips) * sum(get_or_create_output(1).chips) * sum(get_or_create_output(2).chips)
print(result)
