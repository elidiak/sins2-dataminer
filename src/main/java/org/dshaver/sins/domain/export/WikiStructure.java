package org.dshaver.sins.domain.export;

import lombok.Data;
import org.dshaver.sins.domain.ingest.unit.Unit;

import java.util.List;

import static java.util.FormatProcessor.FMT;

@Data
public class WikiStructure implements Priced {
    String race;
    String faction;
    String name;
    String credits;
    String metal;
    String crystal;
    String andvar = "";
    String tauranite = "";
    String indurium = "";
    String kalanide = "";
    String quarnium = "";
    String buildtime;
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
    List<WikiWeapon> weapons;
    String civilianslots;
    String militaryslots;

    public WikiStructure(Unit unit) {
        System.out.println(STR."Creating WikiStructure for \{unit.getId()}");
        this.race = unit.getRace();
        if (unit.getFaction() != null) {
            this.faction = unit.getFaction().getFactionName();
        }
        this.name = unit.getName();
        this.durability = FMT."%.0f\{unit.getHealth().getDurability()}";

        if (unit.getBuild() != null) {
            setPrices(unit.getBuild().getPrice(), unit.getBuild().getExoticPrice());
            this.buildtime = FMT."%.0f\{unit.getBuild().getBuildTime()}";
        }

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

        this.description = unit.getDescription();
        
        // Get Carrier capacity
        if(unit.getCarrier() != null){
            this.carrierCapacity = FMT."\{unit.getCarrier().getBaseMaxSquadronCapacity()}";
        }

        if (unit.getWeapons() != null) {
            this.weapons = unit.getWeapons().getWeapons().stream()
                    .map(WikiWeapon::new)
                    .toList();
        }

        if (unit.getStructure() != null && unit.getStructure().getSlotType() != null) {
            switch (unit.getStructure().getSlotType()) {
                case military -> this.militaryslots = Integer.toString(unit.getStructure().getSlotsRequired());
                case civilian -> this.civilianslots = Integer.toString(unit.getStructure().getSlotsRequired());
            }
        }
    }
}
