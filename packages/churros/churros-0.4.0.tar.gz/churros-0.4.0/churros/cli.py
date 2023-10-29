"""
Usage: 
    churros [options] login <username> [<password>]
    churros [options] logout 
    churros [options] me
    churros [options] user <uid>
    churros [options] group <uid>
    churros [options] users <uids>... 
    churros [options] users [-]

Options:
    -j --json   Output as JSON
       --csv    Output as CSV
"""

import asyncio
import getpass
from http import client
import json
import re
from ssl import MemoryBIO
import subprocess
from ast import Dict
from pathlib import Path
from re import U
from sys import stdin
import tempfile
from typing import Any, NamedTuple
from rich.table import Table

from docopt import docopt
from rich import print

from churros import Churros, DownloadablePictureFile, Group

churros = Churros()


def show_picture(object: DownloadablePictureFile):
    filename = object.download_picture_file()
    if not filename:
        return
    subprocess.run(["viu", filename, "-h", "30", "-w", "80"])
    Path(filename).unlink()


def role_emoj(member) -> str:
    if member.president:
        return "👑"
    if member.vice_president:
        return "🌟"
    if member.secretary:
        return "📜"
    if member.treasurer:
        return "💰"


def get_token():
    cache_filepath = Path.home() / ".cache/churros.json"
    if cache_filepath.exists():
        return json.loads(cache_filepath.read_text()).get("token")
    else:
        return None


def json_camelcase_to_snakecase(json: dict[str, Any]) -> dict[str, Any]:
    return {
        re.sub(r"(?<!^)(?=[A-Z])", "_", key).lower(): json_camelcase_to_snakecase(value)
        if isinstance(value, dict)
        else value
        for key, value in json.items()
    }


async def run():
    opts = docopt(__doc__)

    def output(data: Any, message: str):
        if opts["--json"]:
            print(json.dumps(data, indent=4, ensure_ascii=False))
        elif opts["--csv"]:
            if isinstance(data, dict):
                data = [data]
            # print header
            print(",".join(data[0].keys()))
            # print values
            for line in data:
                print(
                    ",".join(
                        [
                            " ".join(v) if isinstance(v, list) else f"{v}"
                            for v in line.values()
                        ]
                    )
                )
        else:
            print(message)

    if token := get_token():
        churros.token = token

    if opts["login"]:
        username = opts["<username>"]
        password = opts["<password>"] or getpass.getpass("Password: ")

        try:
            token = await churros.login(username, password)
        except Exception as error:
            print(error)
            return 1

        cache_filepath = Path.home() / ".cache/churros.json"
        cache_filepath.parent.mkdir(parents=True, exist_ok=True)
        cache_filepath.write_text(
            json.dumps({"token": token}, indent=4, ensure_ascii=False)
        )

        output(
            {"token": token, "cache_filepath": cache_filepath},
            f"Logged in successfully. Token cached to {cache_filepath}.",
        )

    elif opts["logout"]:
        cache_filepath = Path.home() / ".cache/churros.json"
        cache_filepath.unlink(missing_ok=True)
        await churros.logout()
        output({"result": "OK"}, "Logged out successfully.")

    elif opts["me"] or opts["user"]:
        if opts["me"]:
            u = await churros.me()
        else:
            u = await churros.user(opts["<uid>"])

        show_picture(u)

        output(
            u.model_dump(),
            f"""\
{u.full_name}
@{u.uid}

{' '.join([u.email] + u.other_emails)}
{u.phone}
{u.address}
""",
        )

    elif opts["group"]:
        group = await churros.group(opts["<uid>"])
        show_picture(group)

        output(
            group.model_dump(),
            f"""\
[bold]{group.name}[/bold] [dim]{'@' + group.parent.uid + ' > ' if group.parent else ''}@{group.uid}[/dim]
""",
        )

        members_table = Table.grid("", "Role", "Member", padding=(0, 2))
        for member in group.members:
            if member.title == "Membre" and not role_emoj(member): continue
            members_table.add_row(
                role_emoj(member), member.title, member.member.full_name
            )
        print(members_table)

    elif opts["users"]:
        lines = list(stdin.read().splitlines())
        uids = opts["<uids>"] or [l.strip() for l in lines if l.strip()]
        users = []
        for uid in uids:
            u = await churros.user(uid)
            users.append(u.model_dump())
        if opts["--csv"]:
            # Simplify data for CSV output
            users = [
                {
                    k: u.get(k, "")
                    for k in [
                        "uid",
                        "error",
                        "first_name",
                        "last_name",
                        "graduation_year",
                    ]
                }
                | {
                    "major.short_name": u.get("major", {"short_name": ""}).get(
                        "short_name", ""
                    )
                }
                for u in users
            ]
            pass
        output(users, "Use --json or --csv")


def main():
    asyncio.run(run())
