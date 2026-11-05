# Hippo Shelter - Function Plan

## Chosen animal

Hippopotamus (hippo).

## Overall program description

The program helps a hippo shelter organize a normal day. It registers a new arrival, assigns an available enclosure, records a care task, and produces a daily report. Each function handles one small job. A main function calls the helper functions in the order needed.

This is a planning exercise: the function descriptions identify inputs, observable side effects, and returned information. No executable implementation is required by this plan.

## Helper functions

| Description | Name | Inputs | Side effects | Return value |
| --- | --- | --- | --- | --- |
| Create a registration entry for a newly arrived hippo. | `register_hippo` | Hippo's name and age. | None. | A registration entry containing the name and age. |
| Select an available enclosure for the registered hippo. | `assign_enclosure` | Registration entry and available enclosure information. | None. | The assigned enclosure information, or a message that no enclosure is available. |
| Create the day's care task for that hippo. | `plan_care_task` | Registration entry, assigned enclosure, and staff-provided task description. | None. | A care-task entry identifying the hippo, enclosure, and task. |
| Record whether the assigned task has been completed. | `record_care_task` | Care-task entry, completion status, and staff notes. | None. | An updated task entry with its status and notes. |
| Display a summary of the hippo's registration, housing, and daily care. | `display_daily_report` | Registration entry, enclosure information, and updated care-task entry. | Prints the daily report on the screen. | None. |

## Main function

| Description | Name | Inputs | Side effects | Return value |
| --- | --- | --- | --- | --- |
| Coordinate the shelter program by requesting information and calling the helper functions. | `main` | None; it asks staff for the required information. | Displays prompts, reads staff input, and displays the daily report. | None. |

## Order of tasks

1. Start the program.
2. Ask staff for the new hippo's name and age.
3. Call `register_hippo` and keep the registration entry it returns.
4. Ask for available enclosure information and call `assign_enclosure`.
5. If no enclosure is available, display that result and stop. Otherwise, continue with the assigned enclosure.
6. Ask staff for a care-task description and call `plan_care_task`.
7. Ask whether the task is complete and collect any staff notes.
8. Call `record_care_task` and keep the updated task entry it returns.
9. Call `display_daily_report` with the registration, enclosure, and updated task information.
10. Stop the program.

## How the functions work together

`main` acts like the head chef from the class analogy: it coordinates the jobs. The helper functions each handle one specific task. Returned information is passed to the next function that needs it. For example, the registration entry returned by `register_hippo` is used when planning a care task and printing the report. `display_daily_report` has a visible side effect because it prints, but it does not return a new piece of information.
