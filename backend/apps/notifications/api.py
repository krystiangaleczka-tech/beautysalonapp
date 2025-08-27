from ninja import Router

router = Router()

# Placeholder - will be implemented later
@router.get("/health")
def health_check(request):
    return {"status": "ok", "app": "notifications"}
