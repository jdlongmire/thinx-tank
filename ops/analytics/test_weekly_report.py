import datetime as dt
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch
import tempfile

spec = importlib.util.spec_from_file_location('weekly', Path(__file__).with_name('weekly-report.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class ReportTests(unittest.TestCase):
    def test_completed_week_on_monday_and_sunday(self):
        for day in (21, 27):
            start, end = m.period(dt.datetime(2026, 9, day, 9, tzinfo=m.TZ))
            self.assertEqual(start.date(), dt.date(2026, 9, 14))
            self.assertEqual(end.date(), dt.date(2026, 9, 21))

    def test_dst_week_uses_local_boundaries(self):
        start, end = m.period(dt.datetime(2026, 11, 2, 9, tzinfo=m.TZ))
        self.assertEqual((end.timestamp()-start.timestamp())/3600, 169)
        self.assertEqual((start.hour, end.hour), (0, 0))

    def test_delivered_week_is_not_sent_again(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            state = home/'.local/share/thinx-tank-analytics/reports'
            state.mkdir(parents=True)
            start, _ = m.period(dt.datetime.now(m.TZ))
            (state/f'{start.date().isoformat()}.json').write_text('{}')
            with patch.object(m.Path, 'home', return_value=home), patch('sys.argv', ['weekly-report.py', '--send']), patch.object(m, 'request') as request:
                m.main()
                request.assert_not_called()

    def test_no_division_by_zero(self):
        self.assertEqual(m.change(4, 0), 'no prior traffic')
        self.assertEqual(m.change(0, 0), 'unchanged')
        self.assertEqual(m.change(6, 4), '+50%')

    def test_missing_coverage_disclosed(self):
        start, end = m.period(dt.datetime(2026, 9, 21, 9, tzinfo=m.TZ))
        values = dict(pageviews=0, visitors=0, visits=0)
        text = m.report(start, end, values, values)
        self.assertIn('earlier dates have no coverage', text)
        self.assertNotIn('vs prior week', text)

if __name__ == '__main__':
    unittest.main()
