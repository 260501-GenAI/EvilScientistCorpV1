from fastapi import APIRouter, HTTPException

from app.models.item_model import ItemModel

# Check users.py for relevant comments

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

# Temporary DB of evil items
item_database = {
    1: ItemModel(
        id=1,
        name="Embarrassing Moment Rememberizer",
        description="Reminds victims of the incident from kindergarten",
        inventory=5,
        price=49.99
    ),
    2: ItemModel(
        id=2,
        name="Cauliflowerizer",
        description="Turns mashed potatoes into mashed cauliflower",
        inventory=25,
        price=19.99
    ),
    3: ItemModel(
        id=3,
        name="Moon Vaporizer",
        description="Vaporizes moons",
        inventory=2,
        price=5000.00
    )
}

# Get all items (GET request)
@router.get("/")
async def get_all_items():
    return item_database

# Subtract from item inventory (PATCH request)
# This function only updates inventory, so it should be a PATCH request, not a PUT
@router.patch("/{item_id}/decrement_from_inventory/{amount}")
async def decrement_from_inventory(item_id:int, amount:int):

    # Stolen from Yucheng 2026

    # Check if the item exists
    if item_id in item_database:
        # Save the item so we can access the data
        curr_item = item_database[item_id]
        # Make sure inventory won't be < 0
        if curr_item.inventory >= amount:
            curr_item.inventory -= amount
            return {
                "message": f"{curr_item.name} inventory successfully updated!",
                "inventory": curr_item.inventory
            }
        # 409 - conflict: used when there's a conflict between the request and the state of the resource
        raise HTTPException(status_code=409, detail=f"Item with ID {item_id} has insufficient inventory.")
    raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found.")

# Display a variable amount of map elements (GET request with query param)
# Note that we set a limit default of 1, so we'll get just 1 item if no query param is included
@router.get("/some_items")
async def get_some_items(limit:int=1):
    # Turn the map's values into a list, then...
    # return only the amount of elements specified by the limit
    return list(item_database.values())[:limit]
