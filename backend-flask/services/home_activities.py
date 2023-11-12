from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder
from opentelemetry import trace

# HONEYCOMB
tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run():
    # X-RAY
    segment    = xray_recorder.begin_segment('home_activities segment')
    subsegment = xray_recorder.begin_subsegment('home_actvities subsegment')

    # DATA
    now = datetime.now(timezone.utc).astimezone()
    results = [{
        'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'Andrew Brown',
        'message': 'Cloud is fun!',
        'created_at': (now - timedelta(days=2)).isoformat(),
        'expires_at': (now + timedelta(days=5)).isoformat(),
        'likes_count': 5,
        'replies_count': 1,
        'reposts_count': 0,
        'replies': [{
          'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
          'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
          'handle':  'Worf',
          'message': 'This post has no honor!',
          'likes_count': 0,
          'replies_count': 0,
          'reposts_count': 0,
          'created_at': (now - timedelta(days=2)).isoformat()
        }],
      },
      {
        'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
        'handle':  'Worf',
        'message': 'I am out of prune juice',
        'created_at': (now - timedelta(days=7)).isoformat(),
        'expires_at': (now + timedelta(days=9)).isoformat(),
        'likes': 0,
        'replies': []
      },
      {
        'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
        'handle':  'Garek',
        'message': 'My dear doctor, I am just simple tailor',
        'created_at': (now - timedelta(hours=1)).isoformat(),
        'expires_at': (now + timedelta(hours=12)).isoformat(),
        'likes': 0,
        'replies': []
      }
    ]

    # HONEYCOMB
    with tracer.start_as_current_span("home-activities-mock-data"):
      span = trace.get_current_span()
      span.set_attribute("app.branch", "02-01-01-xray-subsegment-trial")
      span.set_attribute("app.now", str(now))
      span.set_attribute("app.result_length", len(results))

    # XRAY
    subsegment.put_metadata('results', results, 'results')

    return results
