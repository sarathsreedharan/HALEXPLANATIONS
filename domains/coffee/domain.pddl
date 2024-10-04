(define (domain Coffee)
  (:requirements :strips)
  (:predicates (have_coffee_bean)
	       (have_instant_coffee)
	       (is_water_heater_working)
	       (coffee_made)
	       (have_ground_coffee_powder)
	       (is_grinder_working)
	       (coffee_machine_working)
	       (have_water)
	       (have_hot_water)
           (has_clean_mug)
	       )

  (:action clean
         :parameters ()
         :precondition (and )
         :effect
         (and
            (has_clean_mug)
         ))


  (:action grind_coffee
	     :parameters ()
	     :precondition (and (have_coffee_bean) (is_grinder_working))
	     :effect
	     (and 
	        (not (have_coffee_bean))
	        (have_ground_coffee_powder)
	     ))
	     
  (:action heat_water
	     :parameters ()
	     :precondition (and (have_water) (is_water_heater_working))
	     :effect
	     (and 
	        (have_hot_water)
	     ))

  (:action prepare_coffee_in_machine
	     :parameters ()
	     :precondition (and (coffee_machine_working) (have_water) (have_ground_coffee_powder) (has_clean_mug))
	     :effect
	     (and 
	        (coffee_made)
	     ))

  (:action prepare-coffee-from-instant
	     :parameters ()
	     :precondition (and (have_instant_coffee) (have_hot_water) (has_clean_mug))
	     :effect
	     (and 
	        (coffee_made)
	     ))

 )

