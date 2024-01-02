# PRIMER - Vzpostavitev povezave z (navideznim) robotskim manipulatorjem in postavitev le-tega v varno pozo

# Pomembne funkcije za delo z manipulatorjem so:
#   * .state() - nam vrne stanje manipulatorja
#   * .joints - nam vrne seznam sklepov ter njihove vrednosti
#   * .move(state) - premakne manipulator v novo stanje "state"
#   * .position(state) - izracuna 3D lego konca manipulatorja za stanje "state"
#   * .solve(position) - izracuna IK za premik manipulatorja v 3D tocko "position"

import manus
import requests

## Vzpostavite povezave s strežnikom
# 'address' zamenjajte z IP-jem vašega navideznega/fizičnega manipulatorja
server = manus.Server(address="192.168.0.103", port=80)



## Inicializacija manipulatorja
manipulator = manus.Manipulator(server)

## Premikanje manipulatorja
# Stanje sklepov za t.i. varno pozo
safe_position = [0.0, 2.6179938316345215, -1.5707963705062866, -1.2217304706573486, 0.0, 0.0, 0.0]
# Izvedba dejanskega premika manipulatorja v varno pozo
print('Moving to the safe/initial position...', end=' ')
manipulator.move(safe_position)
print('Done!')