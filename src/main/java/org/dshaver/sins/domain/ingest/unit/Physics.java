package org.dshaver.sins.domain.ingest.unit;

import lombok.Data;

@Data
public class Physics {
    double maxLinearSpeed;
    boolean canMoveLinear;
    boolean canMoveAngular;
    double timeToMaxLinearSpeed;
    double maxAngularSpeed;
    double timeToMaxAngularSpeed;
}
