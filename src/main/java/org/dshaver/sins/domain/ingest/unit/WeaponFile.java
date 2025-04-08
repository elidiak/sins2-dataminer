package org.dshaver.sins.domain.ingest.unit;

import org.dshaver.sins.domain.ingest.unit.WeaponFile.Firing;

import lombok.Data;

@Data
public class WeaponFile {
    String name;
    String requiredUnitItem;
    String weaponType;
    double range;
    double cooldownDuration;
    double damage;
    double bombingDamage;
    double penetration;
    Firing firing;

    @Data
    public static class Firing {
        String firingType;
        double travelSpeed;
        double chargeDuration;
    }
}
