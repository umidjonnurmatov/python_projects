"""
Simple To-Do CLI app.
Usage examples:
  python todo_cli.py add "Buy milk"
  python todo_cli.py list
  python todo_cli.py list -a
  python todo_cli.py done 2
  python todo_cli.py remove 3
  python todo_cli.py clear --yes
"""

from __future__ import annotations
import argparse
import json
import os
import sys
from datetime import datetime 
from typing import List, Dict, Any

DATA_FILE = os.path.join(os.path.dirname(__file__), "todos.json")

def load_todos() -> List[Dict[str, Any]]:
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []
    
def save_todos(todos: List[Dict[str, Any]]) -> None:
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(todos, f, indent=2, ensure_ascii=False)


def next_id(todos: List[Dict[str, Any]]) -> int:
    if not todos:
        return 1
    return max(t['id'] for t in todos) + 1


def add_task(text: str) -> None:
    todos = load_todos()
    tid = next_id(todos)
    todos.append({
        'id': tid,
        'task': text,
        'done': False,
        'created_at': datetime.utcnow().isoformat() + 'Z'
    })
    save_todos(todos)
    print(f'Added [{tid}] {text}')


def list_tasks(show_all: bool = False) -> False:
    todos = load_todos()
    if not todos:
        print("No tasks yet. Use 'add' to create one.")
        return 
    for t in todos:
        if not show_all and t.get('done'):
            continue
        status = 'x' if t.get('done') else " "
        created = t.get('created_at', "")
        print(f'[{t['id']}] [{status}] {t['task']} (created: {created})')


def mark_done(tid: int) -> None:
    todos = load_todos()
    for t in todos:
        if t["id"] == tid:
            if t.get("done"):
                print(f"Task [{tid}] is already done.")
            else:
                t["done"] = True
                save_todos(todos)
                print(f"Marked [{tid}] done.")
            return
    print(f"No task with id {tid} found.")



def remove_task(tid: int) -> None:
    todos = load_todos()
    new = [t for t in todos if t["id"] != tid]
    if len(new) == len(todos):
        print(f"No task with id {tid} found.")
    else:
        save_todos(new)
        print(f"Removed task [{tid}].")



def clear_tasks(yes: bool = False) -> None:
    if not yes:
        ans = input("Are you sure you want to delete ALL tasks? (y/N): ").strip().lower()
        if ans != "y":
            print("Aborted.")
            return
    save_todos([])
    print("All tasks cleared.")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="todo", description="Simple To-Do CLI")
    sub = p.add_subparsers(dest="command")

    pa = sub.add_parser("add", help="Add a task")
    pa.add_argument("text", nargs="+", help="Task text")

    pl = sub.add_parser("list", help="List tasks")
    pl.add_argument("-a", "--all", action="store_true", help="Show all tasks (including done)")

    pd = sub.add_parser("done", help="Mark task done")
    pd.add_argument("id", type=int, help="Task id")

    pr = sub.add_parser("remove", help="Remove task by id")
    pr.add_argument("id", type=int, help="Task id")

    pc = sub.add_parser("clear", help="Remove all tasks")
    pc.add_argument("--yes", action="store_true", help="Confirm without prompt")

    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_task(" ".join(args.text))
    elif args.command == "list":
        list_tasks(show_all=args.all)
    elif args.command == "done":
        mark_done(args.id)
    elif args.command == "remove":
        remove_task(args.id)
    elif args.command == "clear":
        clear_tasks(yes=args.yes)
    else:
        parser.print_help()
        sys.exit(1)



if __name__ == "__main__":
    main()