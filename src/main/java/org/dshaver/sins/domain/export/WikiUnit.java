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
    String durability;
    String shield;
    String armor;
    String hull;
    String armorstr;
    String description;
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

        if (unit.getBuild() != null) {
            setPrices(unit.getBuild().getPrice(), unit.getBuild().getExoticPrice());
            this.supply = FMT."\{unit.getBuild().getSupplyCost()}";
            this.buildtime = FMT."%.0f\{unit.getBuild().getBuildTime()}";
        }
        if (unit.getHealth().getLevels().size() > 1) {
            
            Double startShield = unit.getHealth().getLevels().get(0).getMaxShieldPoints();
            Double endShield = unit.getHealth().getLevels().get(9).getMaxShieldPoints();
            this.shield = FMT."%.0f\{startShield} - %.0f\{endShield} (+%.0f\{(endShield - startShield)/9}/lvl)";
           
            Double startArmor = unit.getHealth().getLevels().get(0).getMaxArmorPoints();
            Double endArmor = unit.getHealth().getLevels().get(9).getMaxArmorPoints();
            this.armor = FMT."%.0f\{startArmor} - %.0f\{endArmor} (+%.0f\{(endArmor - startArmor)/9}/lvl)";
            
            Double startHull = unit.getHealth().getLevels().get(0).getMaxHullPoints();
            Double endHull = unit.getHealth().getLevels().get(9).getMaxHullPoints();
            this.hull = FMT."%.0f\{startHull} - %.0f\{endHull} (+%.0f\{(endHull - startHull)/9}/lvl)";
            
            Double startArmorStr = unit.getHealth().getLevels().get(0).getArmorStrength();
            Double endArmorStr = unit.getHealth().getLevels().get(9).getArmorStrength();
            this.armorstr = FMT."%.0f\{startArmorStr} - %.0f\{endArmorStr} (+%.0f\{(endArmorStr - startArmorStr)/9}/lvl)"; 

        }
        else { 
            this.shield = FMT."%.0f\{unit.getHealth().getLevels().get(0).getMaxShieldPoints()}";
            this.armor = FMT."%.0f\{unit.getHealth().getLevels().get(0).getMaxArmorPoints()}";
            this.hull = FMT."%.0f\{unit.getHealth().getLevels().get(0).getMaxHullPoints()}";
            this.armorstr = FMT."%.0f\{unit.getHealth().getLevels().get(0).getArmorStrength()}"; 
        }
        
        this.description = unit.getDescription();

        if (unit.getWeapons() != null) {
            this.weapons = unit.getWeapons().getWeapons().stream()
                    .map(WikiWeapon::new)
                    .toList();
        }
    }
}
