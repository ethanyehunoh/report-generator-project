"""
Squadron Activity Report Generator

This script demonstrates how to use the report_functions module
to generate a comprehensive squadron activity report.

Students will build this step-by-step in the assignment.
"""

import report_functions as rf


def generate_squadron_report(squadron_code, output_file):
    """
    Generates a comprehensive activity report for a specific squadron.
    
    Args:
        squadron_code (str): Squadron identifier (e.g., 'VFA-41')
        output_file (str): Path to save the report
    """
    # TODO: PART 1 - Load the data files
    aircraft = rf.read_csv_file("../data/aircraft.csv")
    flight_log = rf.read_csv_file("../data/flight_logs.csv")
    pilots = rf.read_csv_file("../data/pilots.csv")

    # TODO: PART 2 - Filter data for the specified squadron
    squadron_pilots = rf.filter_by_field(pilots, "squadron", squadron_code)

    # TODO: PART 3 - Get flights for squadron pilots
    squadron_flights = []
    for pilot in squadron_pilots:
        pilot_flights = rf.filter_by_field(flight_log, "pilot_id", pilot["pilot_id"])
        for flight in pilot_flights:
            squadron_flights.append(flight)

    # TODO: PART 4 - Calculate statistics
    pilot_count = rf.count_records(squadron_pilots)
    flight_count = rf.count_records(squadron_flights)
    total_hours = rf.calculate_total(squadron_flights, "duration_hours")
    average_hours = rf.calculate_average(squadron_flights, "duration_hours")

    # TODO: PART 5 - Build the report content
    header = rf.format_header(f"Squadron Report: {squadron_code}")
    statistics = (
        f" Pilots - {pilot_count}\n"
        f" Flight Count - {flight_count}\n"
        f" Total Flight Hours - {total_hours}\n"
        f" Average Flight Hours - {average_hours}\n"
    )

    squadron_report_content = f"{header}\n{statistics}"

    # TODO: PART 6 - Write the report to file
    rf.write_report_to_file(output_file, squadron_report_content)
    print("Report successfully written to file")


# Main execution
if __name__ == '__main__':
    # TODO: Students will customize this to generate reports for different squadrons
    print("Generating squadron activity reports...")
    
    # Example: Generate report for VFA-41 (Black Aces)
    generate_squadron_report('VFA-41', '../reports/vfa-41-report.txt')
    
    # print("\nImplement the function above, then uncomment to test!")
