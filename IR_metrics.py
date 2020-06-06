# Original Note: Created on 25.11.2016  @author: ludewig
# Original Link: https://github.com/leonvking0/Recommendation_Algos
# Modified By LetMe-GX
# Licensed under the Apache License, Version 2.0 (the "License") (added by LetMe-GX)


class MRR:
    """
    MRR( length=20 )

    Used to iteratively calculate the average mean reciprocal rank for a result list with the defined length.

    Parameters
    -----------
    length : int
        MRR@length
    """

    def __init__(self, length=20):
        self.length = length
        self.test = 0
        self.pos = 0

    def init(self, train):
        """
        Do initialization work here.

        Parameters
        --------
        train: pandas.DataFrame
            Training data. It contains the transactions of the sessions.
            It has one column for session IDs, one for item IDs and one for the timestamp of the events
            (unix timestamps).
            It must have a header. Column names are arbitrary, but must correspond to the ones you set during
            the initialization of the network (session_key, item_key, time_key properties).
        """
        return

    def reset(self):
        """
        Reset for usage in multiple evaluations
        """
        self.test = 0
        self.pos = 0

    def skip(self, for_item=0, session=-1):
        pass

    def add(self, result, next_item):
        """
        Update the metric with a result set and the correct next item.
        Result must be sorted correctly.

        Parameters
        --------
        next_item: the item to be located on the candidate item list
        result: pandas.Series
            Series of scores with the item id as the index
        """
        res = result[:self.length]

        self.test += 1

        if next_item in res.index:
            rank = res.index.get_loc(next_item) + 1
            self.pos += (1.0 / rank)

    def add_batch(self, result, next_item):
        """
        Update the metric with a result set and the correct next item.

        Parameters
        --------
        result: pandas.DataFrame
            Prediction scores for selected items for every event of the batch.
            Columns: events of the batch; rows: items. Rows are indexed by the item IDs.
        next_item: Array of correct next items
        """
        i = 0
        for part, series in result.iteritems():
            result.sort_values(part, ascending=False, inplace=True)
            self.add(series, next_item[i])
            i += 1

    def result(self):
        """
        Return a tuple of a description string and the current averaged value
        """
        return ("MRR@" + str(self.length) + ": "), (self.pos / self.test)


class HitRate:
    """
    HR( length=20 )

    Used to iteratively calculate the average hit rate for a result list with the defined length.

    Parameters
    -----------
    length : int
        HitRate@length
    """

    def __init__(self, length=20):
        self.length = length
        self.test = 0
        self.hit = 0

    def init(self, train):
        """
        Do initialization work here.

        Parameters
        --------
        train: pandas.DataFrame
            Training data. It contains the transactions of the sessions. It has one column for session IDs, one for
            item IDs and one for the timestamp of the events (unix timestamps).
            It must have a header. Column names are arbitrary, but must correspond to the ones you set during the
            initialization of the network (session_key, item_key, time_key properties).
        """
        return

    def reset(self):
        """
        Reset for usage in multiple evaluations
        """
        self.test = 0
        self.hit = 0

    def add(self, result, next_item):
        """
        Update the metric with a result set and the correct next item.
        Result must be sorted correctly.

        Parameters
        --------
        next_item: the item to be located on the candidate item list
        result: pandas.Series
            Series of scores with the item id as the index
        """
        self.test += 1

        if next_item in result[:self.length].index:
            self.hit += 1

    def add_batch(self, result, next_item):
        """
        Update the metric with a result set and the correct next item.

        Parameters
        --------
        result: pandas.DataFrame
            Prediction scores for selected items for every event of the batch.
            Columns: events of the batch; rows: items. Rows are indexed by the item IDs.
        next_item: Array of correct next items
        """
        i = 0
        for part, series in result.iteritems():
            result.sort_values(part, ascending=False, inplace=True)
            self.add(series, next_item[i])
            i += 1

    def result(self):
        """
        Return a tuple of a description string and the current averaged value
        """
        return ("HitRate@" + str(self.length) + ": "), (self.hit / self.test)


class Precision:
    """
    Precision( length=20 )

    Used to calculate the precision of the recommendation results.

    Parameters
    -----------
    length : int
        Precision@length
    """

    def __init__(self, length=20):
        self.length = length
        self.test = 0
        self.hit = 0

    def init(self, train):
        """
        Do initialization work here.

        Parameters
        --------
        train: pandas.DataFrame
            Training data. It contains the transactions of the sessions. It has one column for session IDs, one for
            item IDs and one for the timestamp of the events (unix timestamps).
            It must have a header. Column names are arbitrary, but must correspond to the ones you set during the
            initialization of the network (session_key, item_key, time_key properties).
        """
        return

    def reset(self):
        """
        Reset for usage in multiple evaluations
        """
        self.test = 0
        self.hit = 0

    def add(self, result, next_item):
        """
        Update the metric with a result set and the correct next item.
        Result must be sorted correctly.

        Parameters
        --------
        result: pandas.Series
            Series of scores with the item id as the index
        next_item: the list of next items
        """
        self.test += self.length
        self.hit += len(set(next_item) & set(result[:self.length].index))

    def add_batch(self, result, next_item):
        """
        Update the metric with a result set and the correct next item.

        Parameters
        --------
        result: pandas.DataFrame
            Prediction scores for selected items for every event of the batch.
            Columns: events of the batch; rows: items. Rows are indexed by the item IDs.
        next_item: Array of correct next items
        """
        i = 0
        for part, series in result.iteritems():
            result.sort_values(part, ascending=False, inplace=True)
            self.add(series, next_item[i])
            i += 1

    def result(self):
        """
        Return a tuple of a description string and the current averaged value
        """
        return ("Precision@" + str(self.length) + ": "), (self.hit / self.test)


class Recall:
    """
    Recall( length=20 )

    Used to calculate the recall of the recommendation results.

    Parameters
    -----------
    length : int
        Recall@length
    """

    def __init__(self, length=20):
        self.length = length
        self.test = 0
        self.hit = 0

    def init(self, train):
        """
        Do initialization work here.

        Parameters
        --------
        train: pandas.DataFrame
            Training data. It contains the transactions of the sessions. It has one column for session IDs, one for
            item IDs and one for the timestamp of the events (unix timestamps).
            It must have a header. Column names are arbitrary, but must correspond to the ones you set during the
            initialization of the network (session_key, item_key, time_key properties).
        """
        return

    def reset(self):
        """
        Reset for usage in multiple evaluations
        """
        self.test = 0
        self.hit = 0

    def add(self, result, next_item):
        """
        Update the metric with a result set and the correct next item.
        Result must be sorted correctly.

        Parameters
        --------
        result: pandas.Series
            Series of scores with the item id as the index
        next_item: the list of next items
        """
        self.test += len(set(next_item))
        self.hit += len(set(next_item) & set(result[:self.length].index))

    def add_batch(self, result, next_item):
        """
        Update the metric with a result set and the correct next item.

        Parameters
        --------
        result: pandas.DataFrame
            Prediction scores for selected items for every event of the batch.
            Columns: events of the batch; rows: items. Rows are indexed by the item IDs.
        next_item: Array of correct next items
        """
        i = 0
        for part, series in result.iteritems():
            result.sort_values(part, ascending=False, inplace=True)
            self.add(series, next_item[i])
            i += 1

    def result(self):
        """
        Return a tuple of a description string and the current averaged value
        """
        return ("Recall@" + str(self.length) + ": "), (self.hit / self.test)


class MAP:
    """
    MAP( length=20 )

    Used to iteratively calculate the mean average precision for a result list with the defined length.

    Parameters
    -----------
    length : int
        MAP@length
    """

    def __init__(self, length=20):
        self.length = length
        self.test = 0
        self.pos = 0

    def init(self, train):
        """
        Do initialization work here.

        Parameters
        --------
        train: pandas.DataFrame
            Training data. It contains the transactions of the sessions. It has one column for session IDs, one for
            item IDs and one for the timestamp of the events (unix timestamps).
            It must have a header. Column names are arbitrary, but must correspond to the ones you set during the
            initialization of the network (session_key, item_key, time_key properties).
        """
        return

    def reset(self):
        """
        Reset for usage in multiple evaluations
        """
        self.test = 0
        self.pos = 0

    def skip(self, for_item=0, session=-1):
        pass

    def add(self, result, next_item):
        """
        Update the metric with a result set and the correct next item.
        Result must be sorted correctly.

        Parameters
        --------
        result: pandas.Series
            Series of scores with the item id as the index
        next_item: the list of next items
        """
        sum = 0
        ap_list = []
        for i in range(len(next_item)):
            ap_list.append(self.ap(result, next_item[i]))

        ap_list.sort(reverse=True)
        for i in range(len(ap_list)):
            sum += ap_list[i] * (i+1)

        self.pos += (sum / len(ap_list))
        self.test += 1

    def ap(self, result, next_item):
        """
        Update the metric with a result set and the correct next item.
        Result must be sorted correctly.

        Parameters
        --------
        result: pandas.Series
            Series of scores with the item id as the index
        next_item: the next items
        """
        if next_item in result.index:
            rank = result.index.get_loc(next_item) + 1
            return 1.0 / rank
        else:
            return 0

    def result(self):
        """
        Return a tuple of a description string and the current averaged value
        """
        return ("MAP@" + str(self.length) + ": "), (self.pos / self.test)
