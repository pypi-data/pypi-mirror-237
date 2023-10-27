# Aiy

```python

from aiy.log import logger
from aiy.scheduler import Scheduler, Task

# TTS Task
# ...
class TTSTask(Task):
    role: str
    text: str
    output: str

    def __init__(self, role, text) -> None:
        self.role = role
        self.text = text
        self.output = 'output.wav'
        super()

    def run(self):
        if self.id:
            self.output = f'{OUTPUTS}/{self.id}.wav'
        # real work
        tts(self)

# init scheduler
scheduler = Scheduler()
scheduler.async_run()

# ...
req = scheduler.submit_task(task)
print(req.req_id)

# check the task's status
task = scheduler.check_status(id)
print(task.status)

```
