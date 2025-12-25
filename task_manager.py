"""
Simple Task Manager Application
A command-line tool for managing tasks with priorities
"""

class Task:
    """Represents a single task with title, description, and priority."""
    
    def __init__(self, title, description="", priority="medium"):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
    
    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.title} (Priority: {self.priority})"


class TaskManager:
    """Manages a collection of tasks."""
    
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, description="", priority="medium"):
        """Add a new task to the manager."""
        if not title:
            raise ValueError("Task title cannot be empty")
        
        if priority not in ["low", "medium", "high"]:
            raise ValueError("Priority must be low, medium, or high")
        
        task = Task(title, description, priority)
        self.tasks.append(task)
        return task
    
    def get_task(self, index):
        """Get a task by index."""
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range")
        return self.tasks[index]
    
    def complete_task(self, index):
        """Mark a task as completed by index."""
        task = self.get_task(index)
        task.mark_complete()
        return task
    
    def get_pending_tasks(self):
        """Return all pending (incomplete) tasks."""
        return [task for task in self.tasks if not task.completed]
    
    def get_completed_tasks(self):
        """Return all completed tasks."""
        return [task for task in self.tasks if task.completed]
    
    def get_high_priority_tasks(self):
        """Return all high priority tasks."""
        return [task for task in self.tasks if task.priority == "high"]
    
    def count_tasks(self):
        """Return the total number of tasks."""
        return len(self.tasks)


def main():
    """Main entry point for the application."""
    manager = TaskManager()
    
    # Add some sample tasks
    manager.add_task("Complete assignment", "Finish the CI/CD assignment", "high")
    manager.add_task("Buy groceries", "Milk, eggs, bread", "medium")
    manager.add_task("Read a book", "Finish reading 'Clean Code'", "low")
    
    # Display tasks
    print("📋 Task Manager")
    print("=" * 50)
    for i, task in enumerate(manager.tasks):
        print(f"{i + 1}. {task}")
    
    print(f"\nTotal tasks: {manager.count_tasks()}")
    print(f"Pending tasks: {len(manager.get_pending_tasks())}")


if __name__ == "__main__":
    main()