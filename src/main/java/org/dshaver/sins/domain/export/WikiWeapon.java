package org.dshaver.sins.domain.export;

import lombok.Data;
import org.dshaver.sins.domain.ingest.unit.Weapon;

import static java.util.FormatProcessor.FMT;

@Data
public class WikiWeapon {
    String name;
    String requiredUnitItem;
    String weaponType;
    String burstCount;
    String burstDuration;
    String dps;
    String damage;
    String bombingDamage;
    String penetration;
    String cooldownDuration;
    String travelSpeed;
    String range;
    int count;

    String firingType;
    String spawnedUnit;
    String missileDuration;
    String bypassShieldsChance;

    public WikiWeapon(Weapon gameFileWeapon) {
        this.name = gameFileWeapon.getName();
        this.requiredUnitItem = gameFileWeapon.getRequiredUnitItem();
        this.weaponType = gameFileWeapon.getWeaponType();

        if (gameFileWeapon.getBurstCount() > 0) {
            this.burstCount = FMT."%.0f\{gameFileWeapon.getBurstCount()}";
            this.burstDuration = FMT."%.2f\{gameFileWeapon.getBurstDuration()}";
        }
        else {
            this.burstCount = null;
            this.burstDuration = null;
        }

        this.dps = FMT."%.1f\{gameFileWeapon.getDps()}";
        this.damage = FMT."%.0f\{gameFileWeapon.getDamage()}";
        this.bombingDamage = FMT."%.0f\{gameFileWeapon.getBombingDamage()}";
        this.penetration = FMT."%.0f\{gameFileWeapon.getPenetration()}";
        this.cooldownDuration = FMT."%.1f\{gameFileWeapon.getCooldownDuration()}";
        this.travelSpeed = FMT."%.0f\{gameFileWeapon.getTravelSpeed()}";
        this.range = FMT."%.0f\{gameFileWeapon.getRange()}";
        this.count = gameFileWeapon.getCount();

        this.firingType = FMT."%s\{gameFileWeapon.getFiringType()}";
        if (gameFileWeapon.getSpawnedUnit() != null) {
            this.spawnedUnit = FMT."%s\{gameFileWeapon.getSpawnedUnit()}";
            this.missileDuration = FMT."%.1f\{gameFileWeapon.getMissileDuration()}";
        }
        this.bypassShieldsChance = FMT."%.1f\{gameFileWeapon.getBypassShieldsChance()}";
    }
}
