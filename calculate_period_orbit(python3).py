#Calculate the orbital period of a celestial body in sun orbit
from math import pi
import logging
import csv

LOG_FORMAT = "%(levelname)s %(asctime)s -> %(message)s"
logging.basicConfig(filename="Calculate_period.log", level=logging.DEBUG, format=LOG_FORMAT, filemode='w')

logger = logging.getLogger()

#Sun mass
M = 1.989E+30 #Kg

#Gravitational constant
G = 6.67408E-11 #m^3 kg^-1 s^-2

namefile_semimajor_axis = input("Insert the name of file: ")

file_input = open(namefile_semimajor_axis, 'r')

semimajors_axis = file_input.readlines()
semimajors_axis_in_meters = []
name_comet = []

for semimajor_axis in semimajors_axis:
	comet = semimajor_axis.split("|")
	name_comet.append(comet[0])
	semimajor_axis_f = float(comet[1])
	semimajors_axis_in_meters.append(149597870700 * semimajor_axis_f)

def calc(semimajor_axis):
	P = ((4*(pi**2)*(semimajor_axis**3))/(G*M))**(1./2.)
	return P

file_output = open("period.csv", 'w')

writer = csv.writer(file_output)
writer.writerow(["Periodo em anos", "nome cometa"])

count_name_comet = 0
for semimajor_axis_in_meters in semimajors_axis_in_meters:
	period_in_seconds = calc(semimajor_axis_in_meters)
	period_in_years = period_in_seconds/31622400
	writer.writerow([str(period_in_years), str(name_comet[count_name_comet])])
	count_name_comet += 1


