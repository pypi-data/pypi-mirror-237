# Copyright (C) 2023 Bootloader.  All rights reserved.
#
# This software is the confidential and proprietary information of
# Bootloader or one of its subsidiaries.  You shall not disclose this
# confidential information and shall use it only in accordance with the
# terms of the license agreement or other applicable agreement you
# entered into with Bootloader.
#
# BOOTLOADER MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE
# SUITABILITY OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR
# A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.  BOOTLOADER SHALL NOT BE
# LIABLE FOR ANY LOSSES OR DAMAGES SUFFERED BY LICENSEE AS A RESULT OF
# USING, MODIFYING OR DISTRIBUTING THIS SOFTWARE OR ITS DERIVATIVES.

import logging
import re
import subprocess
from os import PathLike
from tempfile import TemporaryFile, NamedTemporaryFile

from majormode.perseus.model.date import ISO8601DateTime

from bootloader.utils.plasticscm.model import Changeset
from bootloader.utils.plasticscm.model import ChangesetDetail


REGEX_PATTERN_DIFFSTAT_OUTPUT = r'\s*\d+.*changed,\s+(?P<lines_inserted>\d*)\s+insertion.*(?P<lines_deleted>\d+)\s+deletion.*'
REGEX_DIFFSTAT_OUTPUT = re.compile(REGEX_PATTERN_DIFFSTAT_OUTPUT)


def convert_to_plastics_scm_timestamp(timestamp: ISO8601DateTime) -> str:
    """

    :param timestamp:
    :return:
    """
    plastic_scm_timestamp = f'{timestamp.year:>04}-{timestamp.month:>02}-{timestamp.day:>02}'

    if hasattr(plastic_scm_timestamp, 'hour'):
        plastic_scm_timestamp += f' {timestamp.hour:>02}:{timestamp.minute:>02}:{timestamp.second:>02}'
    else:
        plastic_scm_timestamp += ' 00:00:00'

    return plastic_scm_timestamp


def get_cm_version() -> str:
    command_line = ['cm', 'version']

    logging.debug(f"Running the command line '{' '.join(command_line)}'...")
    result = subprocess.run(
        command_line,
        capture_output=True,
        text=True
    )

    if result.returncode > 0:
        raise Exception(result.stderr)

    return result.stdout.strip()


def fetch_available_repositories(server_address: str = None) -> list[str]:
    """
    Return the list of available repositories.

    The Plastic SCM server address is also known as the "repository server
    spec" (``repserverspec``).  It can be represented with the string
    ``repserver:name:port``. For examples:

    ```text
    repserver:skull:8084
    skull:8084
    ```

    Plastic SCM call it "repository server spec", instead of just "server
    spec" for historical reasons.  Long ago, they had separate workspace
    and repository servers, and the naming survived.


    :param server_address The hostname and port of the Plastic SCM server
        to connect to and return the list of available repositories.  When
        not defined, the default server is used, i.e., the server
        configured in the configuration wizard and is written in the local
        ``client.conf`` file.


    :return: An array of the names of available repositories.
    """
    command_line = ['cm', 'repository', 'list']
    if server_address is not None:
        command_line.append(server_address)

    logging.debug(f"Running the command line '{' '.join(command_line)}'...")
    result = subprocess.run(
        command_line,
        capture_output=True,
        text=True
    )

    if result.returncode > 0:
        raise Exception(result.stderr)

    return result.stdout.strip().split('\n')


def fetch_changeset_details(
        changeset: Changeset,
        include_file_diff_stats: bool = False
) -> list[ChangesetDetail]:
    """
    Return the list of files and lines that have been changed in the
    specified changeset.


    :param changeset: The changeset to return detailed information.

    :param include_file_diff_stats: Indicate whether to include statistics
        about file changes.


    :return: The list of files that have been changed in the changeset.
    """
    command_line = ['cm', 'find', 'revisions']
    # command_line.append(f"where changeset={changeset.changeset_id} and type!='dir'")
    command_line.append(f"where changeset={changeset.changeset_id} and type='txt'")
    command_line.extend(['on', 'repository', f"'{changeset.repository_name}'"])
    command_line.append('--format={item};{type};{size}')
    command_line.append('--nototal')

    logging.debug(f"Running the command line '{' '.join(command_line)}'...")
    result = subprocess.run(
        command_line,
        capture_output=True,
        text=True
    )

    if result.returncode > 0:
        raise Exception(result.stderr)

    changeset_detail_records = result.stdout.strip().split('\n')

    changeset_details = [
        ChangesetDetail.from_csv(record.split(';'))
        for record in changeset_detail_records
        if record != ''
    ]

    if include_file_diff_stats:
        for detail in changeset_details:
            if detail.file_type == 'txt':
                lines_inserted, lines_deleted = fetch_file_diff_stats(detail.file_path, changeset)
                detail.lines_inserted = lines_inserted
                detail.lines_deleted = lines_deleted

    return changeset_details


# Fetch commit history
def fetch_changeset_history(
        repository_name: str,
        end_date: ISO8601DateTime = None,
        include_details: bool = False,
        start_date: ISO8601DateTime = None,
) -> list[Changeset]:
    """
    Return a history of changesets from the specified repository.


    :param repository_name: The name of the Plastic SCM repository to
        return the changeset history.

    :param end_date: The latest date of changesets to return.  This date
        is exclusive, so changesets that were made at this date are not
        returned.

    :param include_details: Indicate to return the details of each
        changeset.

    :param start_date: The earliest date of changesets to return.  This
        date is inclusive, so changesets that were made at this date are
        returned.


    :return: A list of tuple ``(owner, date, changeset_id)``.
    """
    command_line = ['cm', 'find', 'changeset']

    if start_date or end_date:
        filters = []
        if start_date:
            filters.append(f"date >= '{convert_to_plastics_scm_timestamp(start_date)}'")
        if end_date:
            filters.append(f"date < '{convert_to_plastics_scm_timestamp(end_date)}'")

        where_section = f"where {' and '.join(filters)}"
        command_line.append(where_section)

    command_line.extend(['on', 'repository', f"'{repository_name}'"])
    command_line.append('--format={owner};{date};{changesetid}')

    # https://learn.microsoft.com/en-us/system-center/orchestrator/standard-activities/format-date-time?view=sc-orch-2022
    command_line.append('--dateformat=yyyy-MM-dd HH:mm:ss')
    command_line.append('--nototal')

    shell_command_line = ' '.join(command_line)
    logging.debug(f"Running the command line '{shell_command_line}'...")

    result = subprocess.run(
        command_line,
        capture_output=True,
        text=True
    )

    if result.returncode > 0:
        raise Exception(result.stderr)

    changeset_records = result.stdout.strip().split('\n')

    changesets = [
        Changeset.from_csv(
            repository_name,
            record.split(';')
        )
        for record in changeset_records
        if record != ''
    ]

    if include_details:
        for changeset in changesets:
            changeset.details = fetch_changeset_details(changeset, include_file_diff_stats=True)

    return changesets


def fetch_file_diff_stats(file_path_name: PathLike, changeset: Changeset):
    command_line = ['cm', 'diff']
    command_line.append(f'serverpath:{file_path_name}#cs:{changeset.changeset_id}@{changeset.repository_name}')

    shell_command_line = ' '.join(command_line)
    logging.debug(f"Running the command line '{shell_command_line}'...")

    with TemporaryFile() as fd:
        # print(fd.name)
        diff_process = subprocess.run(command_line, stdout=fd)
        if diff_process.returncode > 0:
            # raise Exception(diff_process.stderr)
            return None, None

        fd.seek(0)

        diffstat_process = subprocess.run(
            ['diffstat'],
            stdin=fd,
            stdout=subprocess.PIPE
        )
        if diffstat_process.returncode > 0:
            raise Exception(diff_process.stderr)

        diff_statistics = diffstat_process.stdout.decode('utf-8').strip()
        match = REGEX_DIFFSTAT_OUTPUT.search(diff_statistics)
        if match is None:
            # raise Exception(f"Invalid 'diffstat' result:\n{diff_process.stdout}")
            return None, None

        return (
            int(match.group('lines_inserted')),
            int(match.group('lines_deleted'))
        )
