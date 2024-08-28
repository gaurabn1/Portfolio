from resume.wsgi import app as application

def handler(event, context):
    # Vercel's serverless function needs to call the WSGI app
    from django.core.handlers.wsgi import WSGIHandler
    from django.core.wsgi import get_wsgi_application
    
    # Ensure Django is setup
    application = get_wsgi_application()
    
    # Pass the event and context to the WSGI application
    environ = {**event}  # Map Vercel's event to WSGI environ
    status, headers, body = WSGIHandler().get_response(environ).start_response
    
    # Return the response in a format Vercel expects
    return {
        'statusCode': status,
        'headers': dict(headers),
        'body': body,
    }
