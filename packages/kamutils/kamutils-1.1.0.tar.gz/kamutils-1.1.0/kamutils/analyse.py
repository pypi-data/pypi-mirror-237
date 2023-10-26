# Analyse and data handling module
# see docs. in Readme.md

#-----------------------------------------------------------------------------------------
# Classes
#-----------------------------------------------------------------------------------------

from collections import OrderedDict

class RangeSet:
    __slots__ = ('ranges')
    
    class ContinuousRange:
        # ex_lower_bound / ex_upper_bound : exclusive bound (True / False)
        __slots__ = ('lower_bound', 'ex_lower_bound', 'upper_bound', 'ex_upper_bound', 'label','custom_label','self_gen')
        
        def __init__(self, lower_bound = None, ex_lower_bound = False, upper_bound = None, ex_upper_bound = False, label = None, custom_label = False, self_gen = False):
            self.lower_bound = lower_bound
            self.upper_bound = upper_bound
            self.ex_lower_bound = ex_lower_bound
            self.ex_upper_bound = ex_upper_bound
            self.label = label
            self.custom_label = custom_label
            self.self_gen = self_gen

        def  __repr__(self):
            args_str = ','.join(f"{value}" for value in {slot_name: getattr(self, slot_name) for slot_name in self.__slots__}.values())
            return(f"ContinuousRange({args_str})")

        def bounds_repr(self):
            if self.lower_bound is None or self.ex_lower_bound:
                lst = [self.upper_bound]
            else:
                lst = [self.lower_bound,self.upper_bound]
            if self.custom_label: lst.append(label)
            if len(lst) == 1:
                return f"{lst[0]}"
            else:
                args_str = ','.join(f"{item}" for item in lst)
                return(f"({args_str})")

        def __str__(self):
            return str({slot_name: getattr(self, slot_name) for slot_name in self.__slots__})
    
    def __init__(self,*args):
        key = 0
        # OrderedDict preserves the order in which the keys are inserted
        # OrderedDict allows to get ranges in ascending order with a simple loop over the keys
        self.ranges = OrderedDict()
        prev_upper_bound = None
        for arg in args:
            # Each argument can be :
            # - A single value which represents the upper bound of the interval
            # - A tuple or a list that contains the interval lower and upper bounds
            lower_bound = None
            ex_lower_bound = False
            upper_bound = None
            try:
                bound_idx = 0
                for value in arg:
                    if bound_idx == 0:
                        lower_bound = value
                    elif bound_idx == 1:
                        upper_bound = value
                        if (upper_bound < lower_bound):
                            raise Exception(f"range {arg} : lower bound is greater than the upper bound")
                    else:
                        break # values beyond the second element are ignored
                    bound_idx += 1
                if bound_idx == 1:
                    # if there is only one bound defined, this is by default the upper bound
                    upper_bound = lower_bound
                    lower_bound = None
            except TypeError:
                # If the argument is not iterable, it's considered to be the interval upper bound
                upper_bound = arg
            if upper_bound is None:
                raise Exception(f"range {arg} : upper bound is not defined")
            if (prev_upper_bound is not None) and (prev_upper_bound >= upper_bound):
                raise Exception(f"range {arg} : upper bound should be greater than the previous range upper bound")
            if lower_bound is None:
                if prev_upper_bound is None:
                    label = f"<= {upper_bound}"
                else:
                    lower_bound = prev_upper_bound
                    ex_lower_bound = True
                    label = f"{lower_bound}]..{upper_bound}]"
            else:
                if (prev_upper_bound is not None) and (prev_upper_bound > lower_bound):
                    raise Exception(f"range {arg} : lower bound should be greater than or equal to the previous range upper bound")
                elif (prev_upper_bound is not None) and (prev_upper_bound == lower_bound):
                    # If this interval lower bound is equal to the previous interval upper bound, the lower bound is
                    # considered as exclusive because a value equal to it will be classified in the previous
                    # interval.
                    lower_bound = prev_upper_bound
                    ex_lower_bound = True
                    label = f"{lower_bound}]..{upper_bound}]"
                else:
                    # When the lower bound is defined, a previous interval is generated :
                    # - Either from (- infinite) to the lower bound if it's the first range
                    # - Or from the preceding interval upper bound to the lower bound
                    create_previous_range = True
                    if key == 0:
                        label = f"< {lower_bound}"
                    else:
                        # We dont create an intermediate interval like 'n]..[n' because n value will always 
                        # belongs to the previous range
                        if self.ranges[key-1].upper_bound == lower_bound: 
                            create_previous_range = False
                        else:
                            label = f"{self.ranges[key-1].upper_bound}]..[{lower_bound}"
                    if create_previous_range:
                        if key == 0:
                            self.ranges[key] = RangeSet.ContinuousRange(None,False,lower_bound,True,label,self_gen=True)
                        else:
                            self.ranges[key] = RangeSet.ContinuousRange(self.ranges[key-1].upper_bound,True,lower_bound,True,label,self_gen=True)
                        key += 1
                    label = f"[{lower_bound}..{upper_bound}]"
            self.ranges[key] = RangeSet.ContinuousRange(lower_bound,ex_lower_bound,upper_bound,False,label)
            prev_upper_bound = upper_bound
            key += 1
        if prev_upper_bound is None:
            raise Exception(f"{args} : empty RangeSet is not allowed")
        # Creation of an extra interval from upper bound to +infinity
        self.ranges[key] = RangeSet.ContinuousRange(prev_upper_bound,True,None,False,f"> {prev_upper_bound}",self_gen=True)
        
    def  __repr__(self):
        args_str = ','.join(range.bounds_repr() for range in self.ranges.values() if not range.self_gen)
        return f"RangeSet({args_str})"

    def __len__(self): # Implements Python's len() function 
        return len(self.ranges)

    def __iter__(self): # RangeSet is Iterable
        for range in self.ranges.items():
            yield range

    def label(self,level):
        return self.ranges[level].label

    def range(self,level):
        return self.ranges[level]

    def first_level(self):
        return 0
        
    def last_level(self):
        # next(reversed(odict)) returns the last (key, value) pair
        return next(reversed(self.ranges.items()))[0]
        
    def level(self,value): # Return the key (level) of the range the value falls in
        for key, range in self.ranges.items():
            if ((range.upper_bound is None) or \
                (range.ex_upper_bound and (value < range.upper_bound)) or \
                ((not range.ex_upper_bound) and (value <= range.upper_bound))) and \
               ((range.lower_bound is None) or \
                (range.ex_lower_bound and (value > range.lower_bound)) or \
                ((not range.ex_lower_bound) and (value >= range.lower_bound))):
                    return key
        # next(reversed(odict)) returns the last (key, value) pair
        return next(reversed(self.ranges.items()))[0]

