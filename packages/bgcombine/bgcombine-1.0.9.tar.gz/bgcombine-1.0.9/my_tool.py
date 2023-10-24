import click
import app.attendance as attendance
import app.personal_info_all_data as info
import app.enrollment as enrollment
import app.cumulative_count as cumulative_count

@click.command()
@click.argument('mode')
@click.option('--o')
@click.option('--c')
@click.option('--filtered')
@click.option('--blacklist', is_flag=True)
@click.version_option('1.0.9')
def main(mode, o, c, filtered, blacklist):
    match mode:
        case 'info':
            pth_in = click.prompt("\n--------------------------------------------------\nenter path to child and family data input folder")
            info.main(pth_in, o)
        case 'attendance':
            pth_in = click.prompt("\n--------------------------------------------------\nenter path to attendance data input folder")
            attendance.main(pth_in, o, filtered, c)
        case 'enrollment':
            pth_in = click.prompt("\n--------------------------------------------------\nenter path to enrollment student list file")
            enrollment.main(pth_in, o)
        case 'cumulative':
            pth_in = click.prompt("\n--------------------------------------------------\nenter path to enrollment student list file")
            cumulative_count.main(pth_in, o, blacklist)
        case _:
            click.echo(f'{mode} is not a supported mode. Type --help for accepted commands.')
        