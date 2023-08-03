from dataclasses import dataclass
from enum import Enum
import random


class CoinYield(Enum):
    H = "H"
    T = "T"


@dataclass(frozen=True)
class SnowWhiteWakeUp:
    H: int = 0
    T1: int = 0
    T2: int = 0


def perform_transition(
    coin_yield: CoinYield, snow_white_wakeup: SnowWhiteWakeUp
) -> SnowWhiteWakeUp:
    if coin_yield == CoinYield.H:
        return SnowWhiteWakeUp(
            H=snow_white_wakeup.H + 1,
            T1=snow_white_wakeup.T1,
            T2=snow_white_wakeup.T2,
        )

    first = SnowWhiteWakeUp(
        H=snow_white_wakeup.H,
        T1=snow_white_wakeup.T1 + 1,
        T2=snow_white_wakeup.T2,
    )
    return SnowWhiteWakeUp(
        H=first.H,
        T1=first.T1,
        T2=first.T2 + 1,
    )


def running_events(events_number: int = 100000) -> SnowWhiteWakeUp:
    sww = SnowWhiteWakeUp()

    for _ in range(events_number):
        coin_yield: CoinYield = random.choice([CoinYield.H, CoinYield.T])
        sww = perform_transition(coin_yield=coin_yield, snow_white_wakeup=sww)

    return sww


if __name__ == "__main__":
    print(running_events())

    # SnowWhiteWakeUp(H=49923, T1=50077, T2=50077)
