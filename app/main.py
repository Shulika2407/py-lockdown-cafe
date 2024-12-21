from app.cafe import Cafe
from app.errors import NotVaccinatedError, NotWearingMaskError


def go_to_cafe(self, friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
            return f"Friends can go to {cafe.name}"
        except NotWearingMaskError:
            masks_to_buy += 1
        except NotVaccinatedError:
            return "All friends should be vaccinated"
    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"
