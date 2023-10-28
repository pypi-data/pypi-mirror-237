import pandas as pd
from tqdm import tqdm
from Database_comparator.config_class import cfg
import os
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast.Applications import NcbimakeblastdbCommandline

import Database_comparator.Fasta_maker as Fasta_maker
import Database_comparator.db_aligner as db_aligner

FastaSeparator = "!"


class blast:
    """
    The blast class provides methods for performing BLAST (Basic Local Alignment Search Tool) searches
    and analyzing the results.

    It can create BLAST databases, perform BLAST searches with provided query sequences, and analyze the
    search results, including inserting matching results into the input DataFrame based on the provided
    configuration.
    """
    def __init__(self, config: cfg, aligner: db_aligner.aligner) -> None:
        self.config = config
        self.aligner = aligner

    # PUBLIC Blast algorithm
    def blast_database_info(self):
        """
        Print information about inserted databases for blast search.

        Note:
            This method prints information about the databases used for BLAST searches, including matrix, gap penalties,
            neighboring words threshold, and window size for multiple hits.
        """
        print("Inserted databases:")
        for database in self.config.in_blast_database:
            print(database)
        print("-----------------------------------------------------")
        print("Matrix: BLOSUM62")
        print("GaPenalties: Existence: 11, Extension: 1")
        print("Neighboring words threshold: 11")
        print("Window for multiple hits: 40")

    def blast_make_database(self, name = "Database", force=False):
        """
        Create a BLAST database with the given name.

        Args:
            name (str): Name of the BLAST database.
            force (bool): Whether to overwrite an existing database and make a new fasta file for all databases (default is False).

        Note:
            This method creates a BLAST database, including the generation of a fasta file from the provided data
            configurations and specified name.
        """
        if not os.path.exists("Fasta_files"):
            os.mkdir("./Fasta_files")
        if not os.path.exists("./Query_files"):
            os.mkdir("./Query_files")

        fasta_file_name = f"Fasta_files/BLAST_fasta_file.fasta"

        if not os.path.exists(fasta_file_name) or force:
            fasta_maker = Fasta_maker.Fasta_maker(
                data_dfs=[pd.DataFrame(pd.read_csv(self.config.data_info[i]["path"], engine="python")) for i in range(len(self.config.data_info))],
                sequence_column_names=[self.config.data_info[i]["sequence_column_name"] for i in range(len(self.config.data_info))],
                identifiers=[self.config.data_info[i]["identifier_of_seq"] for i in range(len(self.config.data_info))],
                result_columns=[self.config.data_info[i]["results_column"] for i in range(len(self.config.data_info))],
                output_file_name=fasta_file_name,
                separator=FastaSeparator)

            fasta_maker.make_file()
        cline = NcbimakeblastdbCommandline(dbtype="prot", input_file=fasta_file_name, input_type="fasta", title=name, max_file_sz="2GB", out=self.config.blast_database_full_name)
        cline()

    def blast_search_for_match_in_database(self, query=None):
        """
        Perform a BLAST search in a BLAST database.

        Args:
            query (str or None): Path to the query sequence file (default is None, uses default input query).

        Note:
            This method performs a BLAST search against the specified database, using the provided query sequence
            or the default input query.
        """
        print(f"Blasting against {self.config.blast_database_full_name}")

        if query is None:
            fasta_maker = Fasta_maker.Fasta_maker(
                data_dfs=[self.config.input_df],
                sequence_column_names=[self.config.input_file_info["sequence_column_name"]],
                identifiers=[],
                result_columns=[],
                output_file_name=self.config.blast_default_input_query,
                separator=FastaSeparator)
            fasta_maker.make_query()
            query = self.config.blast_default_input_query

        blast_in = query
        blast_out = self.config.blast_output_name
        blastp_cline = NcbiblastpCommandline(query=blast_in, db=self.config.blast_database_full_name, evalue=self.config.e_value, outfmt=self.config.blast_outfmt, out=blast_out)

        blastp_cline()
        #print(F"Blasting done. Output: {blast_out}")

    def blast_search_and_analyze_matches_in_database(self, query=None):
        """
        Perform a BLAST search in a BLAST database and then analyze the output data.

        Args:
            query (str or None): Path to the query sequence file (default is None, uses default input query).

        Note:
            This method combines BLAST search with the analysis of the search results, including inserting
            matching results into the input DataFrame.
        """
        self.blast_search_for_match_in_database(query)
        self.blast_analyze_output_data()

    def blast_analyze_output_data(self):
        """
        Analyze the output data from a BLAST search and insert results into the input DataFrame.

        Note:
            This method analyzes the output data from a previous BLAST search and inserts matching results
            into the input DataFrame using the specified aligner and configuration settings.
        """
        columns_names = self.config.blast_outfmt.split()
        data = pd.read_csv(self.config.blast_output_name, sep="\t", names=columns_names[1:])
        data_df = pd.DataFrame(data).drop_duplicates(ignore_index=True)
        for i in tqdm(range(len(data_df)), desc="Analyzing BLAST output data with aligner", colour="green"):
            if self.aligner.align_sequences(data_df["qseq"][i], data_df["sseq"][i]):
                self.__insert_blast_results_to_input_df(data_df, i)

    # PRIVATE Blast algorithm
    def __insert_blast_results_to_input_df(self, data_df: pd.DataFrame, index):
        """
        Insert BLAST results into the input DataFrame.

        Args:
            data_df (pd.DataFrame): Data frame containing BLAST results.
            index (int): Index of the result to be inserted.

        Note:
            This private method processes and inserts BLAST search results into the input DataFrame based on the
            specified configuration settings.
        """
        input_seq_index = int(str(data_df["qseqid"][index]).replace("seq", ""))
        labels = data_df["sseqid"][index].split(sep="!")
        sseq = str(data_df["sseq"][index])

        if len(labels) == 2:
            file_name, output_seq_identifier = labels[0], labels[1]
        else:
            file_name = labels[0]
            output_seq_identifier = labels[0]
        output_seq_identifier = ";".join(set(output_seq_identifier.split(sep=";")))
        database_index = self.config.find_database_index(filename=file_name)
        if pd.isnull(self.config.input_df[self.config.data_info[database_index]["results_column"]][input_seq_index]):
            self.config.input_df.loc[input_seq_index, self.config.data_info[database_index]["results_column"]] = f"[seq: {sseq} identifier:{output_seq_identifier}]\n"
        else:
            self.config.input_df.loc[input_seq_index, self.config.data_info[database_index]["results_column"]] = \
                self.config.input_df[self.config.data_info[database_index]["results_column"]][input_seq_index] + f"[seq: {sseq} identifier:{output_seq_identifier}]\n"
    # ------------------------------------------------------------------------------------------------
