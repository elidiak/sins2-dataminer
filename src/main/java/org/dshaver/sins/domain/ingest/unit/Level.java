package org.dshaver.sins.domain.ingest.unit;

import lombok.Data;

@Data
public class Level {

    double maxShieldPoints;
    double maxArmorPoints;
    double maxHullPoints;
    double armorStrength;

    double hullPointRestoreRate;
    double shieldPointRestoreRate;
    double armorPointRestoreRate;

    ShieldBurstRestore shieldBurstRestore;

    UnitModifiers unitModifiers;
    WeaponModifiers weaponModifiers;

}
