class   Pipeline:
    def __init__(self):
        self.steps=[]
        self.next_id=1


    def add_step(self, category,column,method,parameters=None):

        if parameters is None:
            parameters={}

        step={
            "id":self.next_id,
            "category":category,
            "column":column,
            "method":method,
            "parameters":parameters
        }

        self.steps.append(step)
        self.next_id +=1

    def remove_steps(self,step_id):

        self.steps = [
            step
            for step in self.steps
            if step["id"] != step_id
        ]
    def clear(self):

        self.steps=[]
        self.next_id=1
    def get_steps(self):

        return self.steps

    def move_up(self,step_id):

        for i in range(1,len(self.steps)):

            if self.steps[i]["id"] == step_id:

                self.steps[i - 1],self.steps[i]=(
                    self.steps[i],
                    self.steps[i -1]
                )

                break

    def move_down(self,step_id):

        for i in range(len(self.steps) -1):

            if self.steps[i]["id"] == step_id:

                self.steps[i],self.steps[i + 1]=(
                    self.steps[i + 1],
                    self.steps[i]
                )

                break               
             