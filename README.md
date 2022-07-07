# Scope

Print completed tasks from Todoist account.

Todoist hides completed tasks, but I wanted to know what I've done today, so I wrote this little script which keeps and prints completed tasks.

# Usage

Create a file `token` and paste you Todoist API token in it. You can find it in your Todoist Settings -> Integrations -> API token, https://todoist.com/app/settings/integrations

Run `python show_completed_tasks.py`.

Example:

```
$ python show_completed_tasks.py 
Today:
✅ 15:16:12 | make 1 task for coaching
✅ 14:58:42 | test
✅ 14:41:55 | todoist no hide?
✅ 14:17:05 | write to grandpa
✅ 14:10:26 | therapy and pay @GCal

2022-07-05
✅ 08:43:01 | make 1 task for coaching
```

Run every 2 minutes in bash:
`watch -n 120 "python show_completed_tasks.py"`

# Limitations
On free plan Todoist only keeps 30 completed tasks in its database. This script caches the data when I has it, removing the duplicates, and storing it back to disk. However, if you haven't run it and in the meanwhile completed more than 30 tasks, you will lose some information.

# Future directions
Make it easy to host it as a service and check for completed tasks periodically.
