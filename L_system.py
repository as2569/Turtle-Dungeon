import turtle
import random
import fnmatch
import os

class L_system:        
    def applyRules(self, in_str):
        r = ""
        rand = random.random()
        if fnmatch.fnmatchcase(in_str, '?U?'): # dead end
            r = in_str[0] + '[R1u][1u][L1u]' + in_str[2]
        elif fnmatch.fnmatch(in_str, '?L?'): # room at L
            if rand <= 0.2:
                r = in_str[0] + in_str[1] + 'f' + in_str[2]
            else:
                r = in_str
        elif fnmatch.fnmatch(in_str, '?R?'): # room at R
            if rand <= 0.2:
                r = in_str[0] + in_str[1] + 'f' + in_str[2]
            else:
                r = in_str
        elif fnmatch.fnmatch(in_str, '?u?'): #room at u
            r = in_str[0] + in_str[1] + 'f' + in_str[2]
            #r = in_str
        elif fnmatch.fnmatch(in_str, '2R2'): # left turn
            r = '21L1L1L12' # left hook
        elif fnmatch.fnmatch(in_str, '2L2'): # right turn
            r = '21R1R1R12' # right hook 
        elif fnmatch.fnmatch(in_str, '222'): # 3 long
            r = '2[1R1L2L1R1]1L1R2R1L12' # LR brackets
        elif fnmatch.fnmatch(in_str, '?2?'): # 1 long
            r = in_str[0] + '1f1' + in_str[2] # split long with a room between
        else: # no rule applies
            r = in_str
        return r

    def processSubstring(self, old_str, sub_len):
        new_str = old_str
        fi = 0 # first index
        li = sub_len # last index
        while li <= len(new_str):
            fi += 1
            li += 1
            sub = new_str[fi : li]
            replaced_sub = self.applyRules(sub)
            new_str = new_str[:fi] + replaced_sub + new_str[li:]
            print('sub ' + sub)
            if replaced_sub is not sub:
                print('this ' + sub + ' that ' + replaced_sub)
                fi += len(replaced_sub) - 1
                li += len(replaced_sub) - 1             
        return new_str

    def evolve(self, in_str):
        start_str = in_str
        end_str = self.processSubstring(start_str, 3)
        return end_str
        
