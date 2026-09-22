import datetime as dt
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('digest', Path(__file__).with_name('stats-digest.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class DigestTests(unittest.TestCase):
    def test_stable_tables_and_untrusted_labels(self):
        start=dt.datetime(2026,9,21,tzinfo=m.weekly.TZ)
        days=[((start+dt.timedelta(days=i)).date(),1) for i in range(7)]
        text=m.render(start,start+dt.timedelta(days=7),start,dict(pageviews=7,visitors=2,visits=3),[('/a|<b>\n',7)],[],days)
        self.assertIn('Week end: 2026-09-27',text)
        self.assertIn('/a&#124;&lt;b&gt; ',text)
        self.assertEqual(text.count('## '),4)
        self.assertIn('Partial coverage',text)

    def test_inconsistent_daily_totals_fail(self):
        start=dt.datetime(2026,9,21,tzinfo=m.weekly.TZ)
        with self.assertRaises(ValueError):
            m.render(start,start+dt.timedelta(days=7),start,dict(pageviews=5),[],[],[(start.date(),0)]*7)

    def test_api_failure_never_publishes(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(m.Path,'home',return_value=Path(tmp)), patch('sys.argv',['stats-digest.py','--publish']), patch.object(m,'generate',side_effect=RuntimeError('API unavailable')), patch.object(m,'publish') as publish:
            with self.assertRaises(RuntimeError):m.main()
            publish.assert_not_called()

    def test_metric_validation_sort_limit(self):
        start=dt.datetime(2026,9,21,tzinfo=m.weekly.TZ)
        with patch.object(m.weekly,'request',return_value=[{'x':str(i),'y':i} for i in range(12)]):
            rows=m.metrics(start,start+dt.timedelta(days=7),'path','private')
        self.assertEqual(len(rows),10)
        self.assertEqual(rows[0],('11',11))
        with patch.object(m.weekly,'request',return_value={'error':'unavailable'}):
            with self.assertRaises(ValueError):m.metrics(start,start,'path','private')

if __name__=='__main__':unittest.main()
