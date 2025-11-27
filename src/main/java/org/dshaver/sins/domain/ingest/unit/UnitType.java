package org.dshaver.sins.domain.ingest.unit;

public enum UnitType {
    strikecraft(true, false, false),
    corvette(true, false, false),
    frigate(true, false, false),
    cruiser(true, false, false),
    capital_ship(true, false, false),
    super_capital_ship(true, false, false),
    titan(true, false, false),
    structure(false, true, false),
    starbase(false, true, false),
    torpedo(false, false, true),
    cannon_shell(false, false, false),
    planet(false, false, false),
    asteroid(false, false, false),
    star(false, false, false),
    loot(false, false, false),
    phase_lane(false, false, false),
    gravity_well(false, false, false),
    uncolonizable(false, false, false),
    buff_agent(false, false, false),
    debris(false, false, false),
    untargetable(false, false, false);

    private final boolean ship;
    private final boolean building;
    private final boolean missile;

    UnitType(boolean ship, boolean building, boolean torpedo) {
        this.ship = ship;
        this.building = building;
        this.missile = torpedo;
    }

    public boolean isShip() {
        return (ship || missile);
    }

    public boolean isBuilding() {
        return building;
    }

    public boolean isMissile() {
        return missile;
    }
}
