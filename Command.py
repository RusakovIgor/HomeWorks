class Command:
    def execute(self):
        pass

    def undo(self):
        pass

class MediaPlayer:
    def play(self):
        print("Воспроизведение медиаконтента")

    def pause(self):
        print("Пауза медиаконтента")


class PlayCommand(Command):
    def __init__(self, player: MediaPlayer):
        self.player = player

    def execute(self):
        self.player.play()

    def undo(self):
        self.player.pause()


class PauseCommand(Command):
    def __init__(self, player: MediaPlayer):
        self.player = player

    def execute(self):
        self.player.pause()

    def undo(self):
        self.player.play()

class RemoteControl:
    def __init__(self):
        self.command_history = []

    def execute_command(self, command: Command):
        command.execute()
        self.command_history.append(command)

    def undo_last_command(self):
        if self.command_history:
            last_command = self.command_history.pop()
            last_command.undo()
        else:
            print("Нет команд для отмены")

def main():
    player = MediaPlayer()
    play_command = PlayCommand(player)
    pause_command = PauseCommand(player)

    remote = RemoteControl()

    remote.execute_command(play_command)  # Воспроизведение
    remote.execute_command(pause_command)  # Пауза
    remote.undo_last_command()             # Возвращаем воспроизведение
    remote.undo_last_command()             # Ставим на паузу
    remote.undo_last_command()             # Отмена не сработает, т.к. нет команд

if __name__ == "__main__":
    main()