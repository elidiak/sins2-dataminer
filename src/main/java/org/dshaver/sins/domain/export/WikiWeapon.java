package org.dshaver.sins.domain.export;

import lombok.Data;
import org.dshaver.sins.domain.ingest.unit.Weapon;

import static java.util.FormatProcessor.FMT;

@Data
public class WikiWeapon {
    String name;
    String requiredUnitItem;
    String weaponType;
    String dps;
    String damage;
    String bombingDamage;
    String penetration;
    String cooldownDuration;
    String travelSpeed;
    String range;
    int count;

    public WikiWeapon(Weapon gameFileWeapon) {
        this.name = gameFileWeapon.getName();
        this.requiredUnitItem = gameFileWeapon.getRequiredUnitItem();
        this.weaponType = gameFileWeapon.getWeaponType();
        this.dps = FMT."%.1f\{gameFileWeapon.getDps()}";
        this.damage = FMT."%.0f\{gameFileWeapon.getDamage()}";
        this.bombingDamage = FMT."%.0f\{gameFileWeapon.getBombingDamage()}";
        this.penetration = FMT."%.0f\{gameFileWeapon.getPenetration()}";
        this.cooldownDuration = FMT."%.1f\{gameFileWeapon.getCooldownDuration()}";
        this.travelSpeed = FMT."%.0f\{gameFileWeapon.getTravelSpeed()}";
        this.range = FMT."%.0f\{gameFileWeapon.getRange()}";
        this.count = gameFileWeapon.getCount();
    }


}
