"""
Unit tests for Task Manager Application
"""

import pytest
from task_manager import Task, TaskManager


class TestTask:
    """Test cases for the Task class."""
    
    def test_task_creation(self):
        """Test creating a new task."""
        task = Task("Test task", "Description", "high")
        assert task.title == "Test task"
        assert task.description == "Description"
        assert task.priority == "high"
        assert task.completed is False
    
    def test_task_default_values(self):
        """Test task creation with default values."""
        task = Task("Simple task")
        assert task.description == ""
        assert task.priority == "medium"
    
    def test_mark_complete(self):
        """Test marking a task as complete."""
        task = Task("Test task")
        assert task.completed is False
        task.mark_complete()
        assert task.completed is True
    
    def test_task_string_representation(self):
        """Test the string representation of a task."""
        task = Task("Test task", priority="high")
        result = str(task)
        assert "Test task" in result
        assert "high" in result


class TestTaskManager:
    """Test cases for the TaskManager class."""
    
    def test_add_task(self):
        """Test adding a task to the manager."""
        manager = TaskManager()
        task = manager.add_task("New task", "Description", "high")
        assert manager.count_tasks() == 1
        assert task.title == "New task"
    
    def test_add_task_empty_title(self):
        """Test that empty title raises an error."""
        manager = TaskManager()
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            manager.add_task("")
    
    def test_add_task_invalid_priority(self):
        """Test that invalid priority raises an error."""
        manager = TaskManager()
        with pytest.raises(ValueError, match="Priority must be"):
            manager.add_task("Task", priority="urgent")
    
    def test_get_task(self):
        """Test retrieving a task by index."""
        manager = TaskManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        task = manager.get_task(1)
        assert task.title == "Task 2"
    
    def test_get_task_invalid_index(self):
        """Test that invalid index raises an error."""
        manager = TaskManager()
        manager.add_task("Task 1")
        with pytest.raises(IndexError):
            manager.get_task(5)
    
    def test_complete_task(self):
        """Test completing a task by index."""
        manager = TaskManager()
        manager.add_task("Task 1")
        manager.complete_task(0)
        task = manager.get_task(0)
        assert task.completed is True
    
    def test_get_pending_tasks(self):
        """Test getting pending tasks."""
        manager = TaskManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")
        manager.complete_task(1)
        
        pending = manager.get_pending_tasks()
        assert len(pending) == 2
        assert all(not task.completed for task in pending)
    
    def test_get_completed_tasks(self):
        """Test getting completed tasks."""
        manager = TaskManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.complete_task(0)
        
        completed = manager.get_completed_tasks()
        assert len(completed) == 1
        assert completed[0].title == "Task 1"
    
    def test_get_high_priority_tasks(self):
        """Test getting high priority tasks."""
        manager = TaskManager()
        manager.add_task("Task 1", priority="low")
        manager.add_task("Task 2", priority="high")
        manager.add_task("Task 3", priority="high")
        
        high_priority = manager.get_high_priority_tasks()
        assert len(high_priority) == 2
        assert all(task.priority == "high" for task in high_priority)
    
    def test_count_tasks(self):
        """Test counting total tasks."""
        manager = TaskManager()
        assert manager.count_tasks() == 0
        
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        assert manager.count_tasks() == 2