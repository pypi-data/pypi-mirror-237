# lifeguard-notification-msteams
MS Teams Notifications

## Usage

```python
@validation(
    "Description",
    actions=[notify_in_single_message],
    schedule={"every": {"minutes": 1}},
    settings={
        "notification": {
            "template": "jinja2 string template"
            "msteams": {
                "channels": ["channelwebhookurl"],
            }
        },
    },
)
def a_validation():
    return ValidationResponse("a_validation", NORMAL, {}, {"notification": {"notify": True}})
```
