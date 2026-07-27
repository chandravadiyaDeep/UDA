from analysis.modules.preprocessing.pipeline import Pipeline

pipeline = Pipeline()

print("=" * 60)
print("Empty Pipeline")
print("=" * 60)

print(pipeline.get_steps())

pipeline.add_step(
    category="Missing Values",
    column="Age",
    method="Median"
)

pipeline.add_step(
    category="Encoding",
    column="Sex",
    method="One Hot"
)

pipeline.add_step(
    category="Scaling",
    column="Fare",
    method="StandardScaler"
)

print("\n")
print("=" * 60)
print("After Adding Steps")
print("=" * 60)

for step in pipeline.get_steps():
    print(step)

pipeline.remove_step(2)

print("\n")
print("=" * 60)
print("After Removing Step 2")
print("=" * 60)

for step in pipeline.get_steps():
    print(step)

pipeline.move_down(1)

print("\n")
print("=" * 60)
print("After Moving Down")
print("=" * 60)

for step in pipeline.get_steps():
    print(step)

pipeline.clear()

print("\n")
print("=" * 60)
print("After Clear")
print("=" * 60)

print(pipeline.get_steps())