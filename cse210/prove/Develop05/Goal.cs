public abstract class Goal
{
    public string Name { get; set; }
    protected int Value { get; set; }

    public int GetValue() => Value;

    public Goal(string name, int value)
    {
        Name = name;
        Value = value;
    }

    public abstract void RecordEvent();
    public abstract string GetProgress();
}
