from .extract_feature_alp import aggregate_feature, feature2ALP


class Alp:
    """A class to compute ALP metrics for an event stream.

    ALP is a set of metrics that take BookRoll (ebook) and Moodle activity
    per lecture into account: attendance, report submissions, course views,
    slide views, adding markers or memos, and other actions.
    """

    def __init__(self, course_id):
        """Constructor method

        :param course_id: Number to identify the course data files
        :type course_id: str
        """
        self._course_id = course_id
        self._features_df = aggregate_feature(course_id=course_id)
        self._alp_df, self._alp_df_normalized = feature2ALP(
            features_df=self._features_df
        )

    def _write_csv(self, df, df_type="Alp_Normalized", path=None, filename=None):
        """Writes a CSV file with the contents of `df`, with the specified path and filename.

        :param df: The DataFrame to be written as a CSV file
        :type df: pandas.DataFrame
        :param df_type: String to be included on the output filename, defaults to "Alp_Normalized"
        :type df_type: str, optional
        :param path: Path to the directory where the CSV will be written, defaults to None (present directory)
        :type path: str, optional
        :param filename: Name of the CSV to be written, defaults to None (automatically generated filename)
        :type filename: str, optional
        """
        if filename:
            path_filename = filename
        else:
            path_filename = f"Course_{self.course_id}_{df_type}.csv"
        if path:
            path_filename = f"{path}/{path_filename}"
        df.to_csv(path_filename, index=False)

    def write_features_csv(self, path=None, filename=None):
        """Writes a CSV file with the `self.features_df`, with the specified path and filename.

        :param path: Path to the directory where the CSV will be written, defaults to None (present directory)
        :type path: str, optional
        :param filename: Name of the CSV to be written, defaults to None (automatically generated filename)
        :type filename: str, optional
        """
        self._write_csv(
            self.features_df, df_type="Features", path=path, filename=filename
        )

    def write_alp_csv(self, path=None, filename=None):
        """Writes a CSV file with the `self.alp_df`, with the specified path and filename.

        :param path: Path to the directory where the CSV will be written, defaults to None (present directory)
        :type path: str, optional
        :param filename: Name of the CSV to be written, defaults to None (automatically generated filename)
        :type filename: str, optional
        """
        self._write_csv(self.alp_df, df_type="Alp", path=path, filename=filename)

    def write_alp_normalized_csv(self, path=None, filename=None):
        """Writes a CSV file with the `self.alp_df_normalized`, with the specified path and filename.

        :param path: Path to the directory where the CSV will be written, defaults to None (present directory)
        :type path: str, optional
        :param filename: Name of the CSV to be written, defaults to None (automatically generated filename)
        :type filename: str, optional
        """
        self._write_csv(
            self.alp_df_normalized,
            df_type="Alp_Normalized",
            path=path,
            filename=filename,
        )

    @property
    def course_id(self):
        """Get the course ID.

        :return: The course ID
        :rtype: str
        """
        return self._course_id

    @property
    def features_df(self):
        """Get the features DataFrame

        :return: The features DataFrame
        :rtype: pandas.DataFrame
        """
        return self._features_df

    @property
    def alp_df(self):
        """Get the ALP DataFrame

        :return: The ALP DataFrame
        :rtype: pandas.DataFrame
        """
        return self._alp_df

    @property
    def alp_df_normalized(self):
        """Get the normalized ALP DataFrame

        :return: The normalized ALP DataFrame
        :rtype: pandas.DataFrame
        """
        return self._alp_df_normalized
