package org.dshaver.sins.domain.ingest.unit;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import java.util.List;
import lombok.Data;

@JsonIgnoreProperties
@Data
public class Weapon {
    /**
     * The id such as vasari_heavy_cruiser_medium_wave_cannon. Can be used to lookup the stats in another file.
     */
    String weapon;
    String name;
    String weaponType;
    String requiredUnitItem;
    double burstCount;
    double burstDuration;
    double damage;
    double bombingDamage;
    double penetration;
    double cooldownDuration;
    double travelSpeed;
    double range;
    int count = 1;

    String firingType;
    String spawnedUnit;
    double missileDuration;
    double bypassShieldsChance;

    public void fromWeaponFile(WeaponFile weaponFile, String name) {
        this.name = name;
        this.requiredUnitItem = weaponFile.getRequiredUnitItem();
        this.weaponType = weaponFile.getWeaponType();
        this.damage = weaponFile.getDamage();
        this.bombingDamage = weaponFile.getBombingDamage();
        this.penetration = weaponFile.getPenetration();
        this.cooldownDuration = weaponFile.getCooldownDuration();

        if (weaponFile.getFiring() != null) {
            this.travelSpeed = weaponFile.getFiring().getTravelSpeed();
            this.firingType = weaponFile.getFiring().getFiringType();
            
            if (this.firingType.equals("spawn_torpedo")) {
                this.spawnedUnit = weaponFile.getFiring().getTorpedoFiringDefinition().getSpawnedUnit();
                this.missileDuration = weaponFile.getFiring().getTorpedoFiringDefinition().getDuration();
                this.bypassShieldsChance = weaponFile.getFiring().getTorpedoFiringDefinition().getBypassShieldsChance();
            }
        }
        this.range = weaponFile.getRange();

        if (weaponFile.getBurstPattern() != null) {
            this.burstCount = weaponFile.getBurstPattern().size();
            this.burstDuration = (double) weaponFile.getBurstPattern().get( (int) this.burstCount -1);
        } 
        else {
            this.burstCount = 0;
            this.burstDuration = 0;
        }
    }

    public void add(Weapon identicalWeapon) {
        if (getName().equals(identicalWeapon.getName())) {
            this.count += identicalWeapon.getCount();
        } else {
            System.out.println("Tried to add different weapons together!");
        }
    }

    public double getDps() {
        var selectedDamage = "planet_bombing".equals(getWeaponType()) ? bombingDamage : damage;

        return selectedDamage / cooldownDuration ;
    }

}
