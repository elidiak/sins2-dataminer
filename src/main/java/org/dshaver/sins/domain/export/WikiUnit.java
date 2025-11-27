package org.dshaver.sins.domain.export;

import lombok.Data;
import org.dshaver.sins.domain.ingest.unit.Unit;

import java.util.List;

import static java.util.FormatProcessor.FMT;

@Data
public class WikiUnit implements Priced {
    String race;
    String faction;
    String name;
    String type;
    String credits;
    String metal;
    String crystal;
    String andvar = "";
    String tauranite = "";
    String indurium = "";
    String kalanide = "";
    String quarnium = "";
    String buildtime;
    String supply;
    String speed;
    String timeToMaxLinearSpeed;
    String acceleration;
    String maxAngularSpeed;
    String durability;
    String shield;
    String shieldRegen;
    String shieldBurstCooldown;
    String shieldBurstAmount;
    String armor;
    String armorRegen;
    String hull;
    String hullRegen;
    String armorstr;
    String carrierCapacity;
    String antimatter;
    String antimatterRegen;
    String description;
    
    // Strikecraft only
    String squadronSize;
    String strikeCraftKind;

    List<WikiWeapon> weapons;

    public WikiUnit(Unit unit) {
        System.out.println(STR."Creating WikiUnit for \{unit.getId()}");
        this.race = unit.getRace();
        if (unit.getFaction() != null) {
            this.faction = unit.getFaction().getFactionName();
        }
        this.name = unit.getName();
        this.type = unit.getTargetFilterUnitType();
        this.durability = FMT."%.0f\{unit.getHealth().getDurability()}";
        this.speed = FMT."%.0f\{unit.getModifiedSpeed()}";
        this.timeToMaxLinearSpeed = FMT."%.1f\{unit.getPhysics().getTimeToMaxLinearSpeed()}";
        this.maxAngularSpeed = FMT."%.1f\{unit.getPhysics().getMaxAngularSpeed()}";

        if (unit.getBuild() != null) {
            setPrices(unit.getBuild().getPrice(), unit.getBuild().getExoticPrice());
            this.supply = FMT."\{unit.getBuild().getSupplyCost()}";
            this.buildtime = FMT."%.0f\{unit.getBuild().getBuildTime()}";
        }

        // Get HP, Shields, Antimatter, and Armor.
        if (unit.getHealth().getLevels().size() > 1) {
            
            Double startShield = unit.getHealth().getLevels().get(0).getMaxShieldPoints();
            Double endShield = unit.getHealth().getLevels().get(9).getMaxShieldPoints();
            this.shield = FMT."%.0f\{startShield} - %.0f\{endShield} (+%.0f\{(endShield - startShield)/9}/lvl)";
           
            Double startShieldRegen = unit.getHealth().getLevels().get(0).getShieldPointRestoreRate();
            Double endShieldRegen = unit.getHealth().getLevels().get(9).getShieldPointRestoreRate();
            this.shieldRegen = FMT."%.1f\{startShieldRegen} - %.1f\{endShieldRegen} (+%.1f\{(endShieldRegen - startShieldRegen)/9}/lvl)";

            Double startArmor = unit.getHealth().getLevels().get(0).getMaxArmorPoints();
            Double endArmor = unit.getHealth().getLevels().get(9).getMaxArmorPoints();
            this.armor = FMT."%.0f\{startArmor} - %.0f\{endArmor} (+%.0f\{(endArmor - startArmor)/9}/lvl)";

            Double startArmorRegen = unit.getHealth().getLevels().get(0).getArmorPointRestoreRate();
            Double endArmorRegen = unit.getHealth().getLevels().get(9).getArmorPointRestoreRate();
            this.armorRegen = FMT."%.1f\{startArmorRegen} - %.1f\{endArmorRegen} (+%.1f\{(endArmorRegen - startArmorRegen)/9}/lvl)";
            
            Double startHull = unit.getHealth().getLevels().get(0).getMaxHullPoints();
            Double endHull = unit.getHealth().getLevels().get(9).getMaxHullPoints();
            this.hull = FMT."%.0f\{startHull} - %.0f\{endHull} (+%.0f\{(endHull - startHull)/9}/lvl)";

            Double startHullRegen = unit.getHealth().getLevels().get(0).getHullPointRestoreRate();
            Double endHullRegen = unit.getHealth().getLevels().get(9).getHullPointRestoreRate();
            this.hullRegen = FMT."%.1f\{startHullRegen} - %.1f\{endHullRegen} (+%.1f\{(endHullRegen - startHullRegen)/9}/lvl)";
            
            Double startArmorStr = unit.getHealth().getLevels().get(0).getArmorStrength();
            Double endArmorStr = unit.getHealth().getLevels().get(9).getArmorStrength();
            this.armorstr = FMT."%.0f\{startArmorStr} - %.0f\{endArmorStr} (+%.0f\{(endArmorStr - startArmorStr)/9}/lvl)";
            
            Double startShieldBurstCD = unit.getHealth().getLevels().get(0).getShieldBurstRestore().getCooldownDuration();
            Double endShieldBurstCD = unit.getHealth().getLevels().get(9).getShieldBurstRestore().getCooldownDuration();
            this.shieldBurstCooldown = FMT."%.0f\{startShieldBurstCD}s - %.0f\{endShieldBurstCD}s (%.0f\{(endShieldBurstCD - startShieldBurstCD)/9}s/lvl)";

            Double startShieldBurstAmount = unit.getHealth().getLevels().get(0).getShieldBurstRestore().getRestorePercentage();
            Double endShieldBurstAmount = unit.getHealth().getLevels().get(9).getShieldBurstRestore().getRestorePercentage();
            this.shieldBurstAmount = FMT."%.0f\{startShieldBurstAmount*100}%% - %.0f\{endShieldBurstAmount*100}%% (+%.0f\{(endShieldBurstAmount - startShieldBurstAmount)/9 * 100}%%/lvl)";
            
            Double startAntimatter = unit.getLevels().getLevels().get(0).getUnitModifiers().getAdditiveValues().getMaxAntimatter();
            Double endAntimatter = unit.getLevels().getLevels().get(9).getUnitModifiers().getAdditiveValues().getMaxAntimatter();
            this.antimatter = FMT."%.0f\{startAntimatter} - %.0f\{endAntimatter} (+%.0f\{(endAntimatter - startAntimatter)/9}/lvl)";
            
            Double startAntimatterRegen = unit.getLevels().getLevels().get(0).getUnitModifiers().getAdditiveValues().getAntimatterRestoreRate();
            Double endAntimatterRegen = unit.getLevels().getLevels().get(9).getUnitModifiers().getAdditiveValues().getAntimatterRestoreRate();
            this.antimatterRegen = FMT."%.1f\{startAntimatterRegen} - %.1f\{endAntimatterRegen} (+%.1f\{(endAntimatterRegen - startAntimatterRegen)/9}/lvl)"; 
        }
        else {
            this.shield = FMT."%.0f\{unit.getHealth().getLevels().get(0).getMaxShieldPoints()}";
            this.shieldRegen = FMT."%.1f\{unit.getHealth().getLevels().get(0).getShieldPointRestoreRate()}";
            this.armor = FMT."%.0f\{unit.getHealth().getLevels().get(0).getMaxArmorPoints()}";
            this.armorRegen = FMT. "%.1f\{unit.getHealth().getLevels().get(0).getArmorPointRestoreRate()}";
            this.hull = FMT."%.0f\{unit.getHealth().getLevels().get(0).getMaxHullPoints()}";
            this.hullRegen = FMT. "%.1f\{unit.getHealth().getLevels().get(0).getHullPointRestoreRate()}";
            this.armorstr = FMT."%.0f\{unit.getHealth().getLevels().get(0).getArmorStrength()}";
            this.antimatter = unit.getAntimatter() != null ? FMT."%.0f\{unit.getAntimatter().getMaxAntimatter()}" : null;
            this.antimatterRegen = unit.getAntimatter() != null ? FMT."%.1f\{unit.getAntimatter().getAntimatterRestoreRate()}" : null;

            if (unit.getHealth().getLevels().get(0).getShieldBurstRestore() != null) {
                this.shieldBurstCooldown = FMT."%.0f\{unit.getHealth().getLevels().get(0).getShieldBurstRestore().getCooldownDuration()}s";
                this.shieldBurstAmount = FMT."%.0f\{unit.getHealth().getLevels().get(0).getShieldBurstRestore().getRestorePercentage() * 100}%%";
            }
        }
        
        this.description = unit.getDescription();

        if (unit.getWeapons() != null) {
            this.weapons = unit.getWeapons().getWeapons().stream()
                    .map(WikiWeapon::new)
                    .toList();
        }
        
        // Get Carrier Capacity
        if (unit.getCarrier() != null && unit.getLevels() != null) {
            if (unit.getLevels().getLevels().size() > 1) {
                int startCarrierCapacity = unit.getLevels().getLevels().get(0).getUnitModifiers().getAdditiveValues().getMaxSquadronCapacity();
                int endCarrierCapacity = unit.getLevels().getLevels().get(9).getUnitModifiers().getAdditiveValues().getMaxSquadronCapacity();
                this.carrierCapacity = FMT."\{startCarrierCapacity} - \{endCarrierCapacity}";
            }
        }
        else if(unit.getCarrier() != null){
            this.carrierCapacity = FMT."\{unit.getCarrier().getBaseMaxSquadronCapacity()}";
        }

        // Get Strikecraft Stats
        if (unit.getStrikecraft() != null) {
            this.squadronSize = FMT. "\{unit.getStrikecraft().getSquadronSize()}";
            this.strikeCraftKind = FMT. "\{unit.getStrikecraft().getKind()}";
            this.buildtime = FMT. "\{unit.getStrikecraft().getBuildTime()}";

        }
    }
}
