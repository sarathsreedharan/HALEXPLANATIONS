(define (problem roverprob1234) (:domain rover)
(:objects
	general - Lander
	rover0 - Rover
	rover0store - Store
	waypoint0 waypoint1 waypoint2 waypoint3 waypoint4  waypoint5 waypoint6 - Waypoint
	objective0 objective1 - Objective
	)
(:init
	(connected waypoint1 waypoint0)
	(connected waypoint0 waypoint1)
	(connected waypoint1 waypoint5)
	(connected waypoint5 waypoint1)

	(connected waypoint2 waypoint0)
	(connected waypoint0 waypoint2)

	(connected waypoint2 waypoint3)
	(connected waypoint3 waypoint2)

	(connected waypoint3 waypoint4)
	(connected waypoint4 waypoint3)
	(connected waypoint6 waypoint4)
	(connected waypoint4 waypoint6)

	(at-rock-sample waypoint5)
	(at-soil-sample waypoint2)
	(at-rock-sample waypoint6)


	(at rover0 waypoint0)
	(available rover0)
	(equipped-for-rock-analysis rover0)
	(equipped-for-soil-analysis rover0)


	(can-traverse rover0 waypoint2 waypoint0)
	(can-traverse rover0 waypoint0 waypoint2)

	(can-traverse rover0 waypoint2 waypoint3)
	(can-traverse rover0 waypoint3 waypoint2)

	(can-traverse rover0 waypoint3 waypoint4)
	(can-traverse rover0 waypoint4 waypoint3)

	(can-traverse rover0 waypoint6 waypoint4)
	(can-traverse rover0 waypoint4 waypoint6)

)

(:goal (and
        (at rover0 waypoint0)
        (have-rock-analysis rover0)
        (have-soil-analysis rover0)
	)
)
)
