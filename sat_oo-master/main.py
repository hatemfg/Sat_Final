from Searches import depth_search, breadth_search, a_star
from Variable import *
import time
import os

__author__ = 'ryuzakinho'
from File import File

os.system("rm Results.csv")
fo = open("Results.csv", "a")
fo.write("Ficher;Profondeur;Largeur;A*_1;A*_2;A*_3\n")
print os.listdir(".")
for nom_fichier in os.listdir("."):
    if ".cnf" in nom_fichier:
        cnf_file = File(nom_fichier)
        clause_list = cnf_file.get_clause_info
        print nom_fichier

        debut = time.clock()
        tup = depth_search(clause_list, cnf_file.get_file_info['nbr_variable'])
        elapsed_prof = time.clock() - debut
        d1 = tup[0].already_assigned_variables
        d2 = tup[1]
        d3 = tup[2]
        d4 = tup[3]
        print elapsed_prof

        debut = time.clock()
        tup = breadth_search(clause_list, cnf_file.get_file_info['nbr_variable'])
        elapsed_larg = time.clock() - debut
        p1 = tup[0].already_assigned_variables
        p2 = tup[1]
        p3 = tup[2]
        p4 = tup[3]
        print elapsed_larg

        debut = time.clock()
        tup = a_star(clause_list, cnf_file.get_file_info['nbr_variable'], 1)
        elapsed_a_star_1 = time.clock() - debut
        a_star_1_1 = tup[0].already_assigned_variables
        a_star_1_2 = tup[1]
        a_star_1_3 = tup[2]
        a_star_1_4 = tup[3]
        print elapsed_a_star_1

        debut = time.clock()
        tup = a_star(clause_list, cnf_file.get_file_info['nbr_variable'], 2)
        elapsed_a_star_2 = time.clock() - debut
        a_star_2_1 = tup[0].already_assigned_variables
        a_star_2_2 = tup[1]
        a_star_2_3 = tup[2]
        a_star_2_4 = tup[3]
        print elapsed_a_star_2

        debut = time.clock()
        tup = a_star(clause_list, cnf_file.get_file_info['nbr_variable'], 3)
        elapsed_a_star_3 = time.clock() - debut
        a_star_3_1 = tup[0].already_assigned_variables
        a_star_3_2 = tup[1]
        a_star_3_3 = tup[2]
        a_star_3_4 = tup[3]
        print elapsed_a_star_3

        temp = nom_fichier+";"+str(elapsed_prof)+";"+str(elapsed_larg)+";"+str(elapsed_a_star_1)+";"\
               +str(elapsed_a_star_2)+";"+str(elapsed_a_star_3)+"\n"
        fo.write(temp)

        #temp = "Clauses sat??;" +str(d1)+";"+str(p1)+";"+str(a_star_1_1)+";"+str(a_star_2_1)+";"+str(a_star_3_1)+"\n"
        #fo.write(temp)

        temp = "Clauses ??;"+str(d2)+";"+str(p2)+";"+str(a_star_1_2)+";"+str(a_star_2_2)+";"+str(a_star_3_2)+"\n"
        fo.write(temp)

        temp = "Clauses ??;" +str(d3)+";"+str(p3)+";"+str(a_star_1_3)+";"+str(a_star_2_3)+";"+str(a_star_3_3)+"\n"
        fo.write(temp)

        temp = "Clauses ??;" +str(d4)+";"+str(p4)+";"+str(a_star_1_4)+";"+str(a_star_2_4)+";"+str(a_star_3_4)+"\n"
        fo.write(temp)

fo.close()



