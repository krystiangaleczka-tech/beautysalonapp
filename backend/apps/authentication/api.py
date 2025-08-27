from ninja import Router

router = Router()

# Placeholder - will be implemented in Task 3
@router.get("/health")
def health_check(request):
    return {"status": "ok", "app": "authentication"}